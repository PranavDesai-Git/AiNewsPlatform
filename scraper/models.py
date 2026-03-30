from django.db import models

class BookMark(models.Model):
    url = models.URLField(max_length=512, blank=False)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    summary = models.TextField()

    def __str__(self):
        return self.title
