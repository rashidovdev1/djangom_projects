from django.urls import path
from testapp.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
]