from django import forms

class TodoForm(forms.Form):
    name = forms.CharField(label="name")
    mail = forms.CharField(label="mail")
    age = forms.IntegerField(label="age")

