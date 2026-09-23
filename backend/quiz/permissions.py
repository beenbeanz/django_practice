from rest_framework.permissions import BasePermission

def has_user_type(user, user_type):
    if not user.is_authenticated:
        return False
    return user.user_type >= user_type


class isStudent(BasePermission):
    def has_permission(self, request, view):
        return has_user_type(request.user, 1)

class isTeacher(BasePermission):
    def has_permission(self, request, view):
        return has_user_type(request.user, 2)