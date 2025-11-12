from django.urls import path
from blog.views import BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
]