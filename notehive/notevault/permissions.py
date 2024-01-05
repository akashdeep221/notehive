from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        note = view.get_object()
        return note.owner == request.user
        