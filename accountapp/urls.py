from django.urls import path
from accountapp.views import Hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', Hello_world, name='hello_world'),

    path('create/', AccountCreateView.as_view(), name='create')
]