from rest_framework import serializers
from .models import Events

class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('event_id', 'title', 'description', 'event_date')
