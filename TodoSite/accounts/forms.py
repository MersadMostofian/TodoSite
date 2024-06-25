from django import forms

class userRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    todos = []


class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
