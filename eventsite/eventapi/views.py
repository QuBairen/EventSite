from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EventSerializer, VisitorSerializer, RegistrationSerializer
from .models import Event, Visitor, Registration

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-name')
    serializer_class = EventSerializer

class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all().order_by('-email')
    serializer_class = VisitorSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all().order_by('-registration_time')
    serializer_class = RegistrationSerializer


