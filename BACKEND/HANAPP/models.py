from django.db import models
from django.forms import ModelForm

# Create your models here.


class Teachers2(models.Model):
			
	AVAILABILITY = models.CharField(max_length=30,blank=True,null=True)
	FIRST_NAME = models.CharField(max_length=25)
	LAST_EDITED = models.DateTimeField(blank=True,null=True)
	LAST_NAME = models.CharField(max_length=25)
	ProfPicHappy = models.ImageField(upload_to='images',blank=True,null=True)
	ProfPicAngry = models.ImageField(upload_to='images',blank=True,null=True)

	MOOD = models.CharField(max_length=25,blank=True,null=True)
	SECURITY_KEY = models.CharField(max_length=25)
	STATUS = models.CharField(max_length=50,blank=True,null=True)

	Time1 = models.TimeField(blank=True,null=True)
	Time2 = models.TimeField(blank=True,null=True)
	Time3 = models.TimeField(blank=True,null=True)
	Time4 = models.TimeField(blank=True,null=True)
	Time5 = models.TimeField(blank=True,null=True)

	def __str__(self):
		return self.FIRST_NAME + " " + self.LAST_NAME

class Announcements(models.Model):

	TITLE = models.CharField(max_length=25,blank=True,null=True)
	CONTENT = models.CharField(max_length=140,blank=True,null=True)
	TIME_POSTED = models.DateTimeField(blank=True,null=True)
	TIME_EXPIRES = models.DateField(blank=True,null=True)

	def __str__(self):
		return self.TITLE