from django.db import models
from django.contrib.auth.models import User

class UserFile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    original_name = models.CharField(max_length=255)
    path = models.FileField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    shared_file = models.BooleanField(default=False)