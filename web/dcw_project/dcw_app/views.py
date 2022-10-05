import requests

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

API_URL = 'http://127.0.0.1:8001'
ENDPOINT = 'patient'


def get_patient_data(id: int) -> dict:
    url = API_URL + '/' + ENDPOINT + '/' + id
    response = requests.get(url)
    if response:
        return response.json()

    return None


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    context = None
    pesel = request.GET.get('pesel')
    if pesel:
        context = get_patient_data(pesel)
    return render(request, 'dcw_app/index.html', context)


def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request=request, template_name="dcw_app/register.html", context={"form": form})
