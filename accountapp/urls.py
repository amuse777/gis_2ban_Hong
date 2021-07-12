from django.urls import path
from accountapp.views import Hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', Hello_world, name='hello_world'),
]