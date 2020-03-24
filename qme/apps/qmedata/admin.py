from django.contrib import admin
from .models import Equipment, Measurements, Calibr, Deviations

admin.site.register(Equipment)
admin.site.register(Measurements)
admin.site.register(Calibr)
admin.site.register(Deviations)


# Register your models here.
