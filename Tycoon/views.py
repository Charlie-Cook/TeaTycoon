from tycoon.models import Member, Supply, Collection, Coffers, SupplyRecord
from django.shortcuts import render, redirect
from django.core.mail import send_mail
import tycoon.helpers as helper


def home_page(request):
    saved_members = Member.objects.all().order_by('name')
    saved_supplies = Supply.objects.all().order_by('name')

    current_coffers = helper.get_latest_coffers_amount()

    return render(request, 'home_page.html', {'tea_coffers': current_coffers, 'members': saved_members,
                                              'supplies': saved_supplies})


def new_member(request):
    name_to_save = request.POST.get('member_text', '')
    Member.objects.create(name=name_to_save)
    return redirect('/')


def collect(request, member_id):
    debtor = Member.objects.get(id=member_id)
    debtor.paid = True
    debtor.save()
    try:
        latest_collection_amount = helper.get_latest_collection_amount()
    except IndexError:
        Collection.objects.create(amount=1.00)
        latest_collection_amount = helper.get_latest_collection_amount()
    latest_coffers_amount = helper.get_latest_coffers_amount()
    new_coffers_amount = latest_collection_amount + latest_coffers_amount
    Coffers.objects.create(amount=new_coffers_amount)
    return redirect('/')


def new_collection(request):
    amount = request.POST.get('collection_amount', '')
    float(amount)
    Collection.objects.create(amount=amount)
    Member.objects.filter(paid=True).update(paid=False)
    return redirect('/send_email')


def new_supply(request):
    name_to_save = request.POST.get('supply_text', '')
    Supply.objects.create(name=name_to_save)
    return redirect('/')


def purchase(request, supply_id):
    amount = request.POST.get('purchase_amount', '')
    current_coffers = helper.get_latest_coffers_amount()
    new_coffers = float(current_coffers) - float(amount)
    Coffers.objects.create(amount=new_coffers)
    item = Supply.objects.get(id=supply_id)
    SupplyRecord.objects.create(name=item.name, cost=amount)
    item.stocked = True
    item.save()
    return redirect('/')


def depleted_supply(request, supply_id):
    item = Supply.objects.get(id=supply_id)
    item.stocked = False
    item.save()
    return redirect('/')


def send_email(request):
    user_emails = list(Member.objects.values_list('email', flat=True))
    print(user_emails)
    amount = helper.get_latest_collection_amount()
    send_mail('Tea Club Collection', 'Dear Tea Club member, the collection for the tea club is due.\n'
              'The amount due is £%s.\nPlease make your payment to Charlie Cook when '
              'possible.' % (str(amount)), '***REMOVED***',
              recipient_list=user_emails, fail_silently=False)
    return redirect('/')
