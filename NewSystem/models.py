from django.db import models
from django.contrib.auth.models import User

class Entry(models.Model):
    entry_title = models.TextField()
    entry = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}' .format(self.id)