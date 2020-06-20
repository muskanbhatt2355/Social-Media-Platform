from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from . import forms
# We are first creating a Sigh-Up view for creating a new User.
# Hence, we'll be using a CreateView which is a view that displays 
# a form for creating an object, redisplaying the form with validation
# errors (if there are any) and saving the object.
# Hence, we also need to render a form which can be used by CreateView
# for creating a new User and that form has to be a sign-up form then.
# Also here we'll be using reverse_lazy.
# reverse_lazy is used for resolving Django URL names into URL paths
# For eg. here, we need to redirect the User to home after successful sign-up 
# So, we'll use reverse_lazy('login') -> URL name as defined in urls.py and not the path.


class SignUp(CreateView):
	# we need to include the form that will be used here.
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'Accounts/signup.html'

