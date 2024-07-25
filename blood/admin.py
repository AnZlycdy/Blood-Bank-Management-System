from django.contrib import admin

from blood.models import BloodRequest, Stock

# Register your models here.
admin.site.register(Stock)
admin.site.register(BloodRequest)
