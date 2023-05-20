# -*- coding: utf8 -*-
from drf_yasg import openapi
from rest_framework import status

from api.docs.paginator import PAGINATOR_INFO

CATEGORY_LIST_VIEW = {
    "operation_id": "Список категорий",
    "operation_description": """
        Выводит список всех категорий
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            "Success",
            openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        []
                    ),
                    page_data=openapi.Schema(type=openapi.TYPE_STRING, example='"[\"1\"]"'),
                    page_info=PAGINATOR_INFO,
                ),
            ),
        )
    },
}