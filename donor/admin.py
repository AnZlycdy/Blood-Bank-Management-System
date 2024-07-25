from django.contrib import admin
from .models import BloodDonate, Donor

# Register your models here.
admin.site.register(Donor)
admin.site.register(BloodDonate)