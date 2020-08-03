from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.views.generic import FormView


class MyRegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/gallery"
    template_name = "registration/register.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)