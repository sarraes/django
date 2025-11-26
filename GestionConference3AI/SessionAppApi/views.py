from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from SessionApp.models import Session
from .serializers import SessionSerializer
 # Assure-toi que le serializer existe

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all().order_by('session_day', 'start_time')
    serializer_class = SessionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['session_day', 'room', 'topic', 'conference', 'conference__name']
    search_fields = ['title', 'topic', 'room', 'conference__name']
    ordering_fields = ['session_day', 'start_time', 'end_time', 'created_at', 'title']
