import os

# CCBV
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Models
from forms.models import Form

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Form
from forms.forms import Form as FormClass

# Utils
from sender.utils import get_current_host


class FormsListView(LoginRequiredMixin, ListView):
    model = Form
    paginate_by = 15
    ordering = ["-created_at"]


class FormsCreateView(LoginRequiredMixin, CreateView):
    model = Form
    form_class = FormClass
    success_url = reverse_lazy("forms:list")
    extra_context = {"action": "create"}


class FormsUpdateView(LoginRequiredMixin, UpdateView):
    model = Form
    form_class = FormClass
    template_name = "forms/form_form.html"
    extra_context = {"action": "update"}

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""

        if "form" not in kwargs:
            kwargs["form"] = self.get_form()

        kwargs["host"] = get_current_host(self.request)

        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse_lazy("forms:update", kwargs={"pk": str(self.kwargs["pk"])})


class FormsDeleteView(LoginRequiredMixin, DeleteView):
    model = Form
    success_url = reverse_lazy("forms:list")
