from django.urls import path
from player import views

app_name = 'player'

urlpatterns = [
    path('login/',views.login,name='login')
]