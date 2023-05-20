from drf_yasg import openapi

PAGINATOR_INFO = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties=dict(
        has_previous=openapi.Schema(type=openapi.TYPE_BOOLEAN, example="false"),
        has_next=openapi.Schema(type=openapi.TYPE_BOOLEAN, example="true"),
        num_page=openapi.Schema(type=openapi.TYPE_STRING, example="1"),
    ),
)