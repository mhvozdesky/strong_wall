from django.urls import path
from .views import GreetingView


urlpatterns = [
    path('greeting/', GreetingView.as_view())
]
