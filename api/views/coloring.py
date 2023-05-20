from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.coloring import COLORING_LIST_VIEW, COLORING_LIST_BY_SEARCH_VIEW
from api.services.coloring.list import ColoringListServices
from api.serializers.coloring.list import ColoringListSerializer
from api.services.coloring.search import SearchServices


class ColoringListView(APIView):

    @swagger_auto_schema(**COLORING_LIST_VIEW)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(ColoringListServices, request.GET.dict() | kwargs)
        return Response(
            {
                "colorings": ColoringListSerializer(outcome.result.get('object_list'), many=True).data,
                'page_data': outcome.result.get('page_range'),
                'page_info': outcome.result.get('page_info'),
            },
            status=status.HTTP_200_OK
        )


class ColoringListBySearchView(APIView):

    @swagger_auto_schema(**COLORING_LIST_BY_SEARCH_VIEW)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(SearchServices, request.GET.dict())
        return Response(
            {
                "Coloring": ColoringListSerializer(outcome.result.get('object_list'), many=True).data,
                'page_data': outcome.result.get('page_range'),
                'page_info': outcome.result.get('page_info'),
            },
            status=status.HTTP_200_OK
        )
