from django import forms
from django.core.exceptions import ValidationError

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise ValidationError("Title cannot be empty.")
        return title

    def clean_desc(self):
        desc = self.cleaned_data.get("desc", "").strip()
        if not desc:
            raise ValidationError("Description cannot be empty.")
        return desc

    def clean_location(self):
        location = self.cleaned_data.get("location", "").strip()
        if not location:
            raise ValidationError("Location cannot be empty.")
        return location

    def clean_date(self):
        event_date = self.cleaned_data.get("date", "").strip()
        if not event_date:
            raise ValidationError("Date cannot be empty.")
        return event_date
