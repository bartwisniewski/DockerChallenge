from django.urls import path
from . import views

urlpatterns = [
    path('patient/<int:pesel>/', views.PatientDetail.as_view()),
]