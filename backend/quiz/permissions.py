from rest_framework.permissions import BasePermission

def has_user_type(user, minimum_role):
    if not user.is_authenticated:
        return False
    return user.role >= minimum_role


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return has_user_type(request.user, 1)

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return has_user_type(request.user, 2)