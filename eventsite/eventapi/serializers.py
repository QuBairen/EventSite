from rest_framework import serializers

from .models import Event, Visitor, Registration


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Event
        fields = ['name','location','id','start_time','end_time','visitors']


class VisitorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Visitor
        fields = ['id','email', 'events']

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Registration
        fields = ['id','visitor', 'event',"registration_time"]
