import jwt

from rest_framework import generics
from django.conf import settings
from dca_app.models import Patient
from dca_app.serializers import PatientSerializer


class PatientDetail(generics.RetrieveAPIView):
    lookup_field = 'pesel'
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        token = request.headers['X-Access-Token']
        try:
            jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            print("expired")
            return 'Signature expired. Please log in again.', 401
        except jwt.InvalidTokenError:
            print("invalid")
            return 'Invalid token. Please log in again.', 401
        return self.retrieve(request, *args, **kwargs)
