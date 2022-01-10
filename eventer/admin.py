from django.contrib import admin

from eventer.models import Address, Event

admin.site.register(Event)
admin.site.register(Address)
# Register your models here.
