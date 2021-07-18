from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user_id.id, filename)

class UserFile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    original_name = models.CharField(max_length=255)
    path = models.FileField(upload_to=user_directory_path)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    shared_file = models.BooleanField(default=False)
