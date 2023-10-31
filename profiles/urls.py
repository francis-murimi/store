from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
    path('user-register/',views.user_register,name='user_register'),
    path('log-in/',views.log_in,name='log_in'),
]
