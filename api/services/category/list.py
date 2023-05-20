from service_objects.services import ServiceWithResult
from models_app.models import Category


class CategoryListService(ServiceWithResult):
    def process(self):
        self.result = self._categories
        return self

    @property
    def _categories(self):
        return Category.objects.all().order_by("name")
