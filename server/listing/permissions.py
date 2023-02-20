from rest_framework import permissions


class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Only authenicated users can get here
        # if request.user.is_authenticated:
        #     return True
        # return False
        return True

    def has_object_permission(self, request, view, obj):
        # GET HEAD OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
