from django.contrib import admin
from tycoon.models import Member, Supply, Coffers, Collection, SupplyRecord


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid', 'email')
    ordering = ['name']
    actions = ['mark_paid']

    def mark_paid(self, request, queryset):
        members_updated = queryset.update(paid=True)
        if members_updated == 1:
            message_bit = "1 member was"
        else:
            message_bit = "{} members were".format(members_updated)
        self.message_user(request, "{} successfully marked as paid.".format(message_bit))


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
