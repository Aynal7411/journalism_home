from django import forms
from django.contrib.auth.forms import UserCreationForm

from.models import CustomUser

class AuthorRegistrationForm(UserCreationForm):

    
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    location = forms.CharField(max_length=100, required=True)
    bio = forms.CharField(max_length=500, required=True)
    profile_picture = forms.ImageField(required=False)
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2024)))
   
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email','bio','location','date_of_birth','profile_picture','password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'location': 'Location',
            'bio': 'Bio',
            'profile_picture': 'Profile Picture',
            'date_of_birth': 'Date of Birth',
        
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }