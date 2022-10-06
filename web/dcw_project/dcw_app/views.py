from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator

from .data_provider import get_patient_data


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):

    template_name = "dcw_app/index.html"

    def get(self, request, *args, **kwargs):
        kwargs['pesel'] = request.GET.get('pesel')
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pesel = kwargs['pesel']
        if pesel:
            context['patient_data'] = get_patient_data(pesel)
            if not context['patient_data']:
                context['data_error'] = True
        return context


class ContactFormView(FormView):
    template_name = 'dcw_app/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
