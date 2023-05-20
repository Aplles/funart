from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.serializers.theme.list import ThemeListSerializer
from api.services.theme.category.list import ThemeListService


class ThemeListView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(ThemeListService, request.GET.dict() | kwargs)
        return Response({
            "themes": ThemeListSerializer(outcome.result["object_list"], many=True).data,
            'page_data': outcome.result.get('page_range'),
            'page_info': outcome.result.get('page_info'),
        }, status=status.HTTP_200_OK)
