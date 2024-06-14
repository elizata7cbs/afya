import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import RegexValidator

class Registry(models.Model):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30, blank=True, null=True)
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(auto_now_add=True)
    description = models.CharField(max_length=500)
    phone_number = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^\d{12}$',
                message='Phone number must be exactly 12 digits and contain only numbers.'
            )
        ]
    )
    def __str__(self):
        return f"{self.firstName} {self.middleName} {self.lastName}"

    class Meta:
        db_table = 'registry'


