from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('vote/<str:poll_id>/', vote, name='vote'),
    path('result/<str:poll_id>/', result, name='results'),
]
