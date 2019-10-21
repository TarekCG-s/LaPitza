from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import BooleanField, CharField, EmailField

class UserRegistrationForm(UserCreationForm):
    email = EmailField()
    agreement = BooleanField(label='I Agree to comply with the conditions and terms of this website')

    class Meta():
        model = User
        fields = ['username','email' ,'password1', 'password2', 'agreement']
