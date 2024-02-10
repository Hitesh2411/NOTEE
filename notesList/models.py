from django.db import models
from django.contrib.auth.models import User

class note(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    notes = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
