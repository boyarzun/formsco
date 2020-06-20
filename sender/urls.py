from django.urls import path
from sender.views import send_email

app_name = "sender"

urlpatterns = [
    path("v1/<uuid:pk>/", send_email, name="api_v1"),
]
