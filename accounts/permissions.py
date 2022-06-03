from django.http import HttpRequest
from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from accounts.models import Account


class IsRH(BasePermission):
    def has_permission(self, request: Request, _):
        user: Account = request.user
        url = HttpRequest.get_full_path(request)
        method = request.method

        if url == '/api/candidates/' and method == 'POST':
            return True

        if not user.is_authenticated:
            return False

        return True