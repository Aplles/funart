from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.services.coloring.list import ColoringListServices
from api.serializers.coloring.list import ColoringListSerializer
from api.services.coloring.search import SearchServices


class ColoringListView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(ColoringListServices, kwargs | {**request.data})
        return Response(
            {
                "Theme": ColoringListSerializer(outcome.result.get('object_list'), many=True).data,
                'page_data': outcome.result.get('page_range'),
                'page_info': outcome.result.get('page_info'),
            },
            status=status.HTTP_200_OK
        )


class ColoringListBySearchView(APIView):

    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(SearchServices, {**request.data})
        return Response(
            {
                "Coloring": ColoringListSerializer(outcome.result.get('object_list'), many=True).data,
                'page_data': outcome.result.get('page_range'),
                'page_info': outcome.result.get('page_info'),
            },
            status=status.HTTP_200_OK
        )
