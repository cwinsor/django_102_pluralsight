from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Invitation(models.Model):
    from_user = models.ForeignKey(
        User,
        related_name='invitations_sent',
        on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User,
        related_name='invitations_received',
        on_delete=models.CASCADE,
        verbose_name='User to invite',
        help_text='Please select the user you want to play a game with',
        )
    message = models.CharField(
        max_length=300,
        verbose_name='Optional Message',
        help_text="It's always nice to add a friendly message!"
        )
    timestamp = models.DateTimeField(auto_now_add=True)
    when_to_play = models.DateTimeField(
        default=timezone.now,
        verbose_name='I can play at:',
        help_text="Recommend a time to play",
        )
