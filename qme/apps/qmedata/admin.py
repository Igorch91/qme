from django.contrib import admin
from .models import Equipment, Measurements, Calibr, Deviations, Service

admin.site.register(Equipment)
admin.site.register(Measurements)
admin.site.register(Calibr)
admin.site.register(Deviations)
admin.site.register(Service)


# Register your models here.
