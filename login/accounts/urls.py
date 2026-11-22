from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("terms/", TemplateView.as_view(template_name="legal/terms.html"), name="terms"),
    path("privacy/", TemplateView.as_view(template_name="legal/privacy.html"), name="privacy"),
    path(
        "forgot-password/",
        TemplateView.as_view(template_name="accounts/forgot_password.html"),
        name="forgot_password",
    ),
]