from service_objects.services import ServiceWithResult

from models_app.models import Coloring


class ColoringAllListServices(ServiceWithResult):

    def process(self):
        self.result = self._get_coloring_list
        return self

    @property
    def _get_coloring_list(self):
        return Coloring.objects.all()
