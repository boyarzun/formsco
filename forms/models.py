import uuid

# Models
from django.db import models


class Form(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reply_to = models.EmailField(
        max_length=128,
        blank=True,
        null=True,
        help_text="Taken from html form name='_replyTo' field.",
    )
    from_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=90)
    to = models.EmailField(max_length=128)
    cc = models.TextField(blank=True, null=True, help_text="Separate by commas.")
    bcc = models.TextField(blank=True, null=True, help_text="Separate by commas.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    re_captcha = models.CharField(
        max_length=40, blank=True, null=True, help_text="Secret Key"
    )
