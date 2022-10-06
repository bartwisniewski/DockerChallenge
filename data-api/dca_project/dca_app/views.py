from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer


class PatientDetail(generics.RetrieveAPIView):
    lookup_field = 'pesel'
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    # permission_classes = [IsAdminUser]


@api_view(['GET'])
def patient_detail(request, pesel):
    """
    Retrieve single patient detail
    """
    print("found")
    try:
        patient = Patient.objects.get(pesel=pesel)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
