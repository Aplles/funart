import io
from functools import lru_cache

from PIL import Image
from django.http import HttpResponse
from service_objects.services import ServiceWithResult
from models_app.models import Coloring


class ColoringDownloadService(ServiceWithResult):

    def process(self):
        self.result = self._response
        return self

    @property
    @lru_cache
    def _coloring(self):
        return Coloring.objects.get(id=self.data['id'])

    @staticmethod
    def _image_byte(coloring):
        image = Image.open(coloring.image)
        image_bytes = io.BytesIO()
        image.save(image_bytes, format='JPEG')
        image_bytes.seek(0)
        return image_bytes

    @property
    def _response(self):
        response = HttpResponse(
            self._image_byte(self._coloring),
            content_type="image/jpeg"
        )
        response["Content-Disposition"] = f"attachment; filename={self._coloring.name}.jpeg"
        return response
