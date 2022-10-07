from django.urls import path
from dca_app.views import PatientDetail

urlpatterns = [
    path('patients/<str:pesel>', PatientDetail.as_view()),
]