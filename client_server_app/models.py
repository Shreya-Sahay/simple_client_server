from django.db import models

# Create your models here.

class User(models.Model):
    service_provider_Type = models.CharField(max_length = 128);

class Service_provider(models.Model):
    type_of_service = models.CharField(max_length = 128);
    service_name = models.CharField(max_length = 128);
    email = models.EmailField(max_length = 264, unique = True);
