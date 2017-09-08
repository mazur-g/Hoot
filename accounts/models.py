from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	image = models.ImageField(
	upload_to="img/",
	default = "img/default2.jpg"
	 )
	hoots = models.IntegerField(default=0)