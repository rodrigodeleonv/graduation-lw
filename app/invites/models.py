import uuid

from django.db import models


class Invite(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=120)
    num_invitations = models.SmallIntegerField(default=1)
    confirmed = models.BooleanField(null=True)
    total_confirmed = models.SmallIntegerField(default=0)
    total_requests = models.IntegerField(default=0)
    table = models.SmallIntegerField(null=True)
    confirm_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
