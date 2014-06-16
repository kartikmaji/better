from django.contrib.auth.models import User
from django.forms import ModelForm

class SignupForm(ModelForm):
	class Meta:
		model=User
		fields=('username','email','password','first_name','last_name')

class LoginForm(ModelForm):
	class Meta:
		model=User
		fields=('username','password')

