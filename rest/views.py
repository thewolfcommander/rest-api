from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets

from .models import Tweet
from .serializers import TweetSerializer

class TweetViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all().order_by('-added')


def test(request):
    return render(request, 'index.html')