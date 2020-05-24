#from django.shortcuts import render
#from django.shortcuts import get_object_or_404
#from rest_framework.response import Response
from rest_framework import viewsets 
from .models import Events
from .serializers import EventsSerializer
#from rest_framework.generics import get_object_or_404
#from rest_framework.renderers import TemplateHTMLRenderer


class EventsViewSet(viewsets.ModelViewSet):

    serializer_class = EventsSerializer
    queryset = Events.objects.all()
'''
class EventsView(viewsets.ViewSet):

    def list (self, request):
        queryset = Events.objects.all()
        serializer = EventsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Events.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = EventsSerializer(user)
        return Response(serializer.data)
'''

'''
    def post(self, request):
        event = request.data.get('event')
        serializer = EventsSerializer(data=event)
        if serializer.is_valid(raise_exception=True):
            event_saved = serializer.save()
        return Response({"success": "Event '{}' created successfully".format(event_saved.title)})

    def put(self, request, pk):
        saved_event = get_object_or_404(Events.objects.all(), pk=pk)
        data = request.data.get('event')
        serializer = EventsSerializer(instance=saved_event, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            event_saved = serializer.save()
        return Response({
            "success": "Event '{}' updated successfully".format(event_saved.title)
        })

    def delete(self, request, pk):
        event = get_object_or_404(Events.objects.all(), pk=pk)
        event.delete()
        return Response({
            "message": "Event with id `{}` has been deleted.".format(pk)
        }, status=204)

class EventDetailView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'event_detail.html'

    def get (self, request, pk):
        event = get_object_or_404(Events.objects.all(), pk=pk)
        serializer = EventsSerializer(event)
        return Response ({'serializer': serializer, 'event': event})


    def post (self, request, pk):
        event = get_object_or_404(Events.objects.all(), pk=pk)
        serializer = EventsSerializer(event, data=request.data)
        if not serializer.is_valid(): 
            return Response ({'serializer': serializer, 'event': event})
        serializer.save()
        return redirect('profile-list')
'''
