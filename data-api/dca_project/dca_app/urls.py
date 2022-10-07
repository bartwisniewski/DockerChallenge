from django.urls import path
from . import views

urlpatterns = [
    path('patient/<str:pesel>', views.PatientDetail.as_view()),
]