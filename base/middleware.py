from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class NoAuthBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        um = get_user_model()
        try:
            return um.objects.get(username='admin')
        except:
            return um.objects.create_superuser('admin', 'admin@myproject.com', 'password')

    def get_user(self, user_id):
        return get_user_model().objects.get(username='admin')
