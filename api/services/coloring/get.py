from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Coloring


class ColoringGetServices(ServiceWithResult):
    id = forms.IntegerField()

    def process(self):
        self.result = self._get_coloring
        return self

    @property
    def _get_coloring(self):
        return Coloring.objects.get(id=self.cleaned_data['id'])
