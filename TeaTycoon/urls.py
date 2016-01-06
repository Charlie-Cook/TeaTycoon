"""TeaTycoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from tycoon import views

# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_page, name='home'),
    url(r'^members/add_member$', views.new_member, name='new_member'),
    url(r'^members/(\d+)/collect$', views.collect, name='collect'),
    url(r'^members/new_collection$', views.new_collection, name='new_collection'),
    url(r'^supplies/add_supply$', views.new_supply, name='new_supply'),
    url(r'^supplies/(\d+)/purchase$', views.purchase, name='purchase'),
    url(r'^supplies/(\d+)/depleted$', views.depleted_supply, name='depleted_supply'),
]
