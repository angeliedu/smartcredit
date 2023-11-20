"""
URL configuration for SmartCredit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.checkout_view, name='checkout'),
    path('login/', views.login_page, name='login_page'),
    path('SignUp/', views.signup_page, name='signup_page'),
    path('ForgotPassword/', views.ForgotPassword, name='ForgotPassword'),
    path('Verification/', views.verification, name='verification_page'),
    #path('verify_verification_code/', views.verify_verification_code, name='verify_verification_code'),
    path('CreditForm/',views.CreditForm,name='CreditForm'),
]
