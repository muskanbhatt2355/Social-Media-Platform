from django.db import models
from django.contrib import auth

# auth.models.User has various built-in fields and attributes which ease our job.
class User(auth.models.User,auth.models.PermissionsMixin):

	def __str__(self):
		return "@{}".format(self.username)
