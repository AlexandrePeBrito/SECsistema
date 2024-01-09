from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Rota para login de usuário
    path("login/", views.login_view, name="login"),

    # Rota para registro de usuário
    path("register/", views.register_user, name="register"),

    # Rota para logout de usuário
    path("logout/", LogoutView.as_view(), name="logout"),
]
