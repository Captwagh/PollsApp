from django.urls import path

from polls.views import welcome

urlpatterns = [
    path('', welcome),
]