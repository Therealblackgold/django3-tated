from django.db import models
from django.utils import timezone


class Side(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='side/images/')
    url_1 = models.URLField(blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
