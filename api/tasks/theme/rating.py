from service_objects.services import ServiceWithResult

from models_app.models import Theme


class ThemeRatingZeroingService(ServiceWithResult):

    def process(self):
        self._zeroing()
        return self

    @property
    def _themes(self):
        return Theme.objects.all()

    def _zeroing(self):
        for them in self._themes:
            them.rating = 0
            them.save()
