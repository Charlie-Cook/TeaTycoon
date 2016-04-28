from django.contrib import admin
from tycoon.models import Member, Supply, Coffers, Collection, SupplyRecord


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid', 'email')


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('name', 'stocked')


@admin.register(Coffers)
class CoffersAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount')


@admin.register(SupplyRecord)
class SupplyRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'cost')
