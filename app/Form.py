from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm

class account_creation_form(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control','id': 'my_field'}))
    password2=None
    class Meta:
        model = User
        fields =['username','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control','id': 'my_field'}),
                'email': forms.EmailInput(attrs={'class':'form-control','id': 'my_field'})}

class login_form(AuthenticationForm):
    username=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class user_change_form(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email','first_name','last_name',]
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                }

class password_form(PasswordChangeForm):
    old_password=None
    new_password1=forms.CharField(label="Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="Confirm Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        
class name_form(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))