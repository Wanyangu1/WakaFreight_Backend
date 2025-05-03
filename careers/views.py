# careers/views.py
from rest_framework import generics
from .models import JobOpening
from .serializers import JobOpeningSerializer

class JobOpeningListAPIView(generics.ListAPIView):
    queryset = JobOpening.objects.all().order_by('-posted')
    serializer_class = JobOpeningSerializer
