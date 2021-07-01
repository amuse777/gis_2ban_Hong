from django.urls import path
from accountapp.views import Hello_world

urlpatterns = [
    path('hello_world/', Hello_world, name='hello_world'),
]