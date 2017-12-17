from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User,Permission
from django.core.validators import MaxValueValidator


class Profile(models.Model):
	userid=User(models.ForeignKey(User))
	first_name=models.CharField(max_length=100,default='Please enter your ')
	last_name=models.CharField(max_length=100,default='Profile')
	birthdate=models.DateField('Date of Birth',default=timezone.now)
	emailid=models.EmailField()
	account_balance = models.IntegerField(default=0)
	account_number = models.IntegerField(default=0)

	def __str__(self):
		return self.first_name+" "+self.last_name