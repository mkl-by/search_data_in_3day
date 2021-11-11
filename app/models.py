from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Purchases(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    money = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    date = models.DateTimeField(default=timezone.now)
