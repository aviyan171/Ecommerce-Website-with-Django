"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include, reverse_lazy
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.forms import MyPasswordResetForm



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name="register"),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='users/passwordchange.html',success_url=reverse_lazy('password_success')),name="changepassword"),
    path('password_success/',auth_views.PasswordChangeDoneView.as_view(template_name='users/passwordchangedone.html'),name="password_success"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html",success_url=reverse_lazy('password_reset_done')),name="password-reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
    path('',include('ElectronicStore.urls'))
]

