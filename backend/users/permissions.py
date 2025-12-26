from rest_framework.permissions import BasePermission

class IsWaiter(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'WAITER'

class IsCashier(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Cashier').exists()

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()