from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView

from .forms import EventForm
from .models import Event


class EventListView(ListView):
    model = Event
    template_name = "beeTheBeet/event_list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "beeTheBeet/event_detail.html"
    context_object_name = "event"


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "beeTheBeet/event_form.html"
    success_url = "/"
