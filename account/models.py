from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

from django.db.models.fields import BigIntegerField
# Create your models here.

class CustomUser(AbstractUser):
# class User(AbstractUser):    
    # temp_id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    temp_id = models.UUIDField(default=uuid.uuid4)
    # address = models.TextField(null=True, blank=True)
    # email = models.EmailField(max_length=30, null=True, blank=True)


    def __str__(self):
        return self.username