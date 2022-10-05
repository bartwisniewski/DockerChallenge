from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.


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
