from django.urls import path
from .views import BaseView, LoginView, RegistrationsView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', BaseView.as_view(), name='main'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationsView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),
]
