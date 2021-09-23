from django.http import HttpRequest

from rest_framework.permissions import BasePermission


class CanCreate(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return request.method == "POST"


class CanRead(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return request.method == "GET"
