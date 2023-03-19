from drf_yasg import openapi


class RequestContentTypes:
    APPLICATION_JSON = "application/json"


class SwaggerRequestParams:
    game_id = openapi.Parameter(
        "game_id", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING
    )
    name = openapi.Parameter(
        "name",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="Optional Parameter",
    )
