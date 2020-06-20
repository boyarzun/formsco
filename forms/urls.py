from django.urls import path
from forms.views import *

app_name = "forms"

urlpatterns = [
    path("", FormsListView.as_view(), name="list"),
    path("new/", FormsCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", FormsUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", FormsDeleteView.as_view(), name="delete"),
]
