from django.urls import path
from . import views
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index),
    path('contact/',views.contact , name = 'contact'),
    path('register/', views.register, name = 'register'),
    path('login/',LoginView.as_view(template_name='pages/login.html') , name = 'login'),
    #auth_views.LoginView.as_view(template_name=template_name)
    #auth_views.login, {'template_name':'pages/login.html'}
    #path('logout/',LogoutView.as_view(template_name='pages/login.html') , name = 'logout')
    path('logout/',LogoutView.as_view(next_page='/') , name = 'logout')
]   