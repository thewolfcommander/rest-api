from django.db import models

class Tweet(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(str(self.id), self.title)