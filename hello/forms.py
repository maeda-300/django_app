from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='email')
    gender = forms.BooleanField(label='Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')