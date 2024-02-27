from rest_framework import permissions
from django.conf import settings


class IsStaffOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method  in permissions.SAFE_METHODS:
            return True
        
        else:
            return request.user.email in settings.ISHIRO_STAFF_EMAIL and request.user.is_staff
