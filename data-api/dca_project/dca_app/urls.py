from django.urls import path
from . import views

urlpatterns = [
    path('patients/<str:pesel>', views.PatientDetail.as_view()),
]