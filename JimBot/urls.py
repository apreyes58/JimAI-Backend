from django.urls import path
from .views import chat_view
from .views import test_view

urlpatterns = [
    path('chat/', chat_view, name = 'chat'),
    path('test/', test_view, name = 'chat_test')
]