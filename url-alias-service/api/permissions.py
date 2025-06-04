from rest_framework.permissions import BasePermission


class IsPublicEndpoint(BasePermission):
    def has_permission(self, request, view):
        return view.__class__.__name__ == 'RedirectView'
