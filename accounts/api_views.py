from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()

class ManageCovidUser(RetrieveUpdateDestroyAPIView):
    queryset = User
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return response

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(data='delete success')