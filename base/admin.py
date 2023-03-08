from django.contrib import admin
from .models import CargoVehicleType, Vehicle


admin.site.register((CargoVehicleType, Vehicle))
