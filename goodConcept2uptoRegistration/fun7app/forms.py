from django import forms
from django.contrib.auth.models import User
from fun7app.models import Father, Student

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password')
        #fields= '__all__'


class StudentProfileInfoForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('NameStudent','aadhaar','profile_pic_blnk')
#email ni maanga...
        #we have not included  user  field...
         # fields = '__all__'   ye nahi karega....bcz allfields
         # cannot be input...it depends on User

# not filling father model?? later karunga
