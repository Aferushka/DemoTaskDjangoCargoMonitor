def start_vehicle_fill(sender, **kwargs):
    from .models import Vehicle, CargoVehicleType
    from .apps import BaseConfig

    if isinstance(sender, BaseConfig):
        belaz, _ = CargoVehicleType.objects.update_or_create(model_name='БЕЛАЗ', defaults={'max_weight': 120})
        komatsu, _ = CargoVehicleType.objects.update_or_create(model_name='Komatsu', defaults={'max_weight': 110})

        Vehicle.objects.update_or_create(bort_number='101', defaults={'model': belaz, 'current_weight': 100})
        Vehicle.objects.update_or_create(bort_number='102', defaults={'model': belaz, 'current_weight': 125})
        Vehicle.objects.update_or_create(bort_number='К103', defaults={'model': komatsu, 'current_weight': 120})

