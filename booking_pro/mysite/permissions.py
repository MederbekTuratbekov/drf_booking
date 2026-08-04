from rest_framework import permissions


class CheckRole(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.hotel_owner == request.user


class CheckUserRoleReviews(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.guest_status == 'owner':
            return False
        return True


class CreatePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.guest_status == 'guest'


class IsHotelOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.guest_status == 'owner')
