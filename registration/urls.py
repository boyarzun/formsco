from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "registration"

urlpatterns = [
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(redirect_authenticated_user=True),
        name="login",
    ),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
]
