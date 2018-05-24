from django.db import models
import bcrypt
from datetime import datetime


# Model - Guide Login
class Guide(models.Model):
    g_name = models.CharField(max_length=255)
    g_email = models.CharField(max_length = 30)
    g_password = models.CharField(max_length = 30)
    g_contact = models.CharField(max_length=255)
    g_description = models.TextField(max_length=255)
    g_aboutme = models.CharField(max_length=255)
    g_created_at = models.DateTimeField(auto_now_add=True)
    g_updated_at = models.DateTimeField(auto_now=True)
    # objects = GuideManager()

# Model - Tourist Login
class Tourist(models.Model):
    t_name = models.CharField(max_length=255)
    t_email = models.CharField(max_length = 30)
    t_password = models.CharField(max_length = 30)
    t_contact = models.CharField(max_length=255)
    t_created_at = models.DateTimeField(auto_now_add=True)
    t_updated_at = models.DateTimeField(auto_now=True)