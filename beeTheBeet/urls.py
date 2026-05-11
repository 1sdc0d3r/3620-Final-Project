from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event_list"),
    path("event/new", views.EventCreateView.as_view(), name="event_new"),
    path("event/<int:pk>", views.EventDetailView.as_view(), name="event_detail"),
]
