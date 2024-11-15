from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

from ksu_events.ksu_events.models.mixins import TimeStampMixin


def validate_date_format(value):
    try:
        datetime.strptime(value, '%m-%d-%Y')
    except ValueError:
        raise ValidationError('Date of Birth must be in MM-DD-YYYY format')


class User(AbstractUser, TimeStampMixin):
    date_of_birth = models.DateField(
        null=True, blank=False, verbose_name='Date of Birth', help_text='MM-DD-YYYY')
    """This class extends the base Django Auth User model to allow for additional fields"""

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.email}"
