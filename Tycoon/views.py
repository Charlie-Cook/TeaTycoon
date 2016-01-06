from django.shortcuts import render, redirect
from tycoon.models import Member, Supply, Collection, Coffers
import datetime as dt


def home_page(request):
    saved_members = Member.objects.all()
    saved_supplies = Supply.objects.all()
    try:
        current_coffers = Coffers.objects.order_by('-id')[0].amount
    except IndexError:
        current_date = dt.datetime.today().strftime('%Y-%m-%d')
        Coffers.objects.create(date=current_date, amount=0)
        current_coffers = Coffers.objects.order_by('-id')[0].amount
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
    date_today = dt.datetime.today().strftime('%Y-%m-%d')
    try:
        latest_collection_amount = Collection.objects.order_by('-id')[0].amount
    except IndexError:
        Collection.objects.create(date=dt.datetime.today().strftime('%Y-%m-%d'), amount=1.00)
        latest_collection_amount = Collection.objects.order_by('-id')[0].amount
    latest_coffers_amount = Coffers.objects.order_by('-id')[0].amount
    new_coffers_amount = latest_collection_amount + latest_coffers_amount
    Coffers.objects.create(date=date_today, amount=new_coffers_amount)
    return redirect('/')


def new_collection(request):
    amount = request.POST.get('collection_amount', '')
    float(amount)
    todays_date = dt.date.today().strftime('%Y-%m-%d')
    Collection.objects.create(date=todays_date, amount=amount)
    Member.objects.filter(paid=True).update(paid=False)
    return redirect('/')


def new_supply(request):
    name_to_save = request.POST.get('supply_text', '')
    Supply.objects.create(name=name_to_save)
    return redirect('/')


def purchase(request, supply_id):
    item = Supply.objects.get(id=supply_id)
    item.stocked = True
    item.save()
    return redirect('/')


def depleted_supply(request, supply_id):
    item = Supply.objects.get(id=supply_id)
    item.stocked = False
    item.save()
    return redirect('/')
