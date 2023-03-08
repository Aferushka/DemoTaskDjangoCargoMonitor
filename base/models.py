from django.db import models


class CargoVehicleType(models.Model):
    model_name = models.CharField(max_length=15, verbose_name='Модель')
    max_weight = models.IntegerField(verbose_name='Грузоподъемность (т)')

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = 'Модель грузовика'
        verbose_name_plural = 'Модели грузовиков'


class Vehicle(models.Model):
    bort_number = models.CharField(max_length=10, verbose_name='Бортовой номер', primary_key=True)
    model = models.ForeignKey('CargoVehicleType', on_delete=models.PROTECT)
    current_weight = models.IntegerField(default=0, verbose_name='Текущий груз (т)')

    @property
    def overweight(self):
        ov = ((100 * self.current_weight) / self.model.max_weight) - 100
        return 0 if ov < 0 else int(ov)

    def __str__(self):
        return f'{self.bort_number} {self.model.model_name}'

    class Meta:
        verbose_name = 'Автопарк'
        verbose_name_plural = 'Автопарк'
