from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(
        upload_to="avatars/", default="default.jpg", blank=True, null=True
    )

    # username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]