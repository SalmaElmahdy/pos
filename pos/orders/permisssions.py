from rest_framework import permissions


#TODO:: separate every permission
class IsCashierOrSupervisor(permissions.BasePermission):

    def has_permission(self, request, view):
        is_supervisor = request.user.groups.filter(name='supervisor').exists()
        
        if is_supervisor:
            return True
        
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.groups.filter(name='cashier').exists()
        
        return request.method in permissions.SAFE_METHODS