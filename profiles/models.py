from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the built-in User model
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(help_text='254xxx',blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
