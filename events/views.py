from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Place, Event

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'latest_events_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Event.objects.filter(
            created__lte=timezone.now()
        ).order_by('-created')[:5]

def index(request):
    all_events = Event.objects.all()
    return render(request, 'events/index.html', {'all_events': all_events})


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Event.objects.filter(created__lte=timezone.now())

class EventView(generic.ListView):
    model = Event
    template_name = 'events/event.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Event.objects.filter(created__lte=timezone.now()).order_by('-created')[:5]


class PlaceView(generic.DetailView):
    model = Place
    template_name = 'events/place.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Place.objects.filter(created__lte=timezone.now()).order_by('-created')[:5]
