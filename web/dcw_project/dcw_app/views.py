import requests

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

API_URL = 'http://127.0.0.1:8001/patient/'
ENDPOINT = 'patient'


def get_patient_data(id: int) -> dict:
    url = API_URL + '/' + ENDPOINT + '/' + id
    response = requests.get(url)
    if response:
        print('Success!')
    else:
        print('An error has occurred.')

    return {'pesel': id, 'first_name': 'Bartosz', 'surname': 'Wisniewski', 'age': 33}


def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    context = None
    pesel = request.GET.get('pesel')
    if pesel:
        context = get_patient_data(pesel)
    print(context)
    return render(request, 'dcw_app/index.html', context)


def register_request(request):
    print("here i am")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request=request, template_name="dcw_app/register.html", context={"form": form})
