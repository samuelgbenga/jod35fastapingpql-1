import typing

from strawberry.permission import BasePermission
from strawberry.types import Info
from src.auth.utils import decode_token


class IsAuthenticated(BasePermission):
    message = "User is not Authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request = info.context["request"]
        # Access headers authentication
        authorization = request.headers["Authorization"]
        if authorization:
            token = authorization.split("Bearer ")[-1]
            return decode_token(token)
        return False