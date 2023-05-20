from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.services.category.list import CategoryListService


class CategoryListView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CategoryListService, {})
        return Response()
