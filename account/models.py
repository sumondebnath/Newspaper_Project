from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="account/images/", null=True, blank=True)

    def __str__(self):
        return self.user.first_name