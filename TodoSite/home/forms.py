from django import forms
from .models import Todo

class createTodoForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField()


class updateTodoForm(forms.ModelForm):
    class  Meta:
        model = Todo
        fields = ('title','body','created')# we can use __all__ instead of ('title','body','created')
