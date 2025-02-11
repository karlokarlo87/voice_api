from django.urls import path

from .views import get_voice, my_api_view

urlpatterns = [
    #path('voice/<str:text>/', get_voice1, name='voice'),
    path('voice/', my_api_view, name='voice'),
    path('get/', get_voice, name='voice'),
]