from django.urls import path
from django.urls import include

from dcw_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register', views.ContactFormView.as_view(), name="register")
]