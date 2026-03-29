from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES=(
    ('admin', 'ADMIN'),
    ('user', 'USER'),
)

class UserModel(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = None
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(choices=ROLES, default='user')