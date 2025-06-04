import string
import random
import uuid
from datetime import timedelta
from django.db import models
from django.utils import timezone


def generate_short_id(length=10):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


class ShortLink(models.Model):
    original_url = models.URLField()
    short_id = models.CharField(max_length=20, unique=True, default=generate_short_id)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=1)
        super().save(*args, **kwargs)

    def is_expired(self):
        return timezone.now() > self.expires_at


class ClickStat(models.Model):
    link = models.ForeignKey(ShortLink, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)
