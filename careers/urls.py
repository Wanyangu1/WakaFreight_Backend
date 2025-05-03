# careers/urls.py
from django.urls import path
from .views import JobOpeningListAPIView

urlpatterns = [
    path('jobs/', JobOpeningListAPIView.as_view(), name='job-list'),
]
