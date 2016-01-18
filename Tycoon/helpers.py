import datetime as dt
from tycoon.models import Coffers, Collection


def get_current_date():
    return dt.date.today().strftime('%Y-%m-%d')


def get_latest_coffers_amount():
    try:
        latest_coffers_amount = Coffers.objects.order_by('-id')[0].amount
    except IndexError:
        Coffers.objects.create(amount=0.00)
        latest_coffers_amount = Coffers.objects.order_by('-id')[0].amount
    return latest_coffers_amount


def get_latest_collection_amount():
    try:
        latest_collection_amount = Collection.objects.order_by('-id')[0].amount
    except IndexError:
        Collection.objects.create(amount=0.00)
        latest_collection_amount = Collection.objects.order_by('-id')[0].amount
    return latest_collection_amount


def get_latest_collection_date():
    try:
        latest_collection_date = Collection.objects.order_by('-id')[0].date
    except IndexError:
        Collection.objects.create(amount=0.00)
        latest_collection_date = Collection.objects.order_by('-id')[0].date
    return latest_collection_date
