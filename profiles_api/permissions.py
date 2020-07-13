from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    # Allow user to edit their own Profile
    def has_object_permission(self,request,view,obj):
        # Check User is Trying to Edit their own Profile
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id
        
