from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(("title"), max_length=50)
    desc = models.CharField(("desc"), max_length=500)
    location = models.CharField(("location"), max_length=50)
    date = models.CharField(("date"), max_length=20)

    def __str__(self):
        return self.title
