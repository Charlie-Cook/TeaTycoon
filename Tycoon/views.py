from django.shortcuts import render, redirect
from tycoon.models import Member, Supply, Collection
import datetime as dt


def home_page(request):
    saved_members = Member.objects.all()
    saved_supplies = Supply.objects.all()
    return render(request, 'home_page.html', {'tea_coffers': '£5', 'members': saved_members, 'supplies': saved_supplies})


def new_member(request):
    name_to_save = request.POST.get('member_text', '')
    Member.objects.create(name=name_to_save)
    return redirect('/')


def collect(request, member_id):
    debtor = Member.objects.get(id=member_id)
    debtor.paid = True
    debtor.save()
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
