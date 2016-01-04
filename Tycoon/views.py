from django.shortcuts import render, redirect
from tycoon.models import Member, Supply


def home_page(request):
    saved_members = Member.objects.all()
    saved_supplies = Supply.objects.all()
    return render(request, 'home_page.html', {'tea_coffers': '£5', 'members': saved_members, 'supplies': saved_supplies})


def new_member(request):
    name_to_save = request.POST.get('member_text', '')
    Member.objects.create(name=name_to_save)
    return redirect('/')


def new_supply(request):
    name_to_save = request.POST.get('supply_text', '')
    Supply.objects.create(name=name_to_save)
    return redirect('/')
