from django.shortcuts import render

from rest_framework import permissions
from rest_framework import viewsets

from .models import Tweet
from .serializers import TweetSerializer

class TweetViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all().order_by('-added')

    def get_queryset(self):
        request = self.request
        qs = Tweet.objects.all()
        query = request.GET.get('search')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs


def test(request):
    return render(request, 'index.html')