from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
     class Meta:
        fields = ('username','email','password1','password2') 
        # password1 and 2 are for password confirmation
        model = get_user_model()