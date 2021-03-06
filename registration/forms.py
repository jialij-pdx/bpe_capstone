# Customize registration forms site.
#
# Bonneville Power Adminstration Front-End
# Copyright (C) 2015  Shu Ping Chu
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm # base auth user form from library
from django.core.exceptions import ValidationError     # validate library

# new add
from .models import UserProfile

# validate email if is unique
def validate_email_unique(value):
    exists = User.objects.filter(email=value)
    if exists:
        raise ValidationError("Email address %s already exists, must be unique" % value)

# Customize registration form that extended from UserCreationFrom which inherit username and password
# "required=true": field cannot empty
# "help_text": description for the field
# "validators": check the field if is valid
class MyRegistrationForm(UserCreationForm):
    register_code = forms.CharField(required=True, help_text = "Code received from BPA administrator")
    email = forms.EmailField(required=True, validators=[validate_email_unique])
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    # Embedded class within the scope of the MyRegistrationForm class, to hold anything from the
    # form field, also can put any attribute in this class
    class Meta:
        model = User  # whose the form is
        fields = ('register_code',
                  'username',
                  'password1',
                  'password2',
                  'email',
                  'first_name',
                  'last_name')
            
        # This is how the user save the form
        def save(self, commit=True):                          
            user = super(UserCreationForm, self).save(commit=False) # not to commit the data since haven't finished the rest of data yet!!
            user.register_code = self.cleaned_data['register_code']
            user.username = self.cleaned_data['username']
            user.password1 = self.cleaned_data['password1']
            user.password2 = self.cleaned_data['password2']
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
          
            # if commit == true
            if commit:  
                user.save()

            return user


# new add
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('cellphone','company',)
