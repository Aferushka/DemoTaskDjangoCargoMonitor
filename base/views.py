from django.views.generic import ListView
from .models import Vehicle, CargoVehicleType


class CargoView(ListView):
    template_name = 'index.html'

    def get_queryset(self, **kwargs):
        model_filter = self.request.GET.get('modelname', '')
        qs = Vehicle.objects.all()
        return qs.filter(model__model_name=model_filter) if model_filter else qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['select_option_list'] = list(CargoVehicleType.objects.values_list('model_name', flat=True))
        context['selected_option'] = self.request.GET.get('modelname', '')
        return context


