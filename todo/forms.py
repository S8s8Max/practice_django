from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name", "mail", "gender", "age", "birthday"]

class TodoForm(forms.Form):
    name = forms.CharField(label="Name", \
        widget=forms.TextInput(attrs={"class":"form-control"}))
    mail = forms.EmailField(label="EMail", \
        widget=forms.EmailInput(attrs={"class":"form-control"}))
    gender = forms.BooleanField(label="Gender", \
        widget=forms.CheckboxInput(attrs={"class":"form-control"}))
    age = forms.IntegerField(label="Age", \
        widget=forms.NumberInput(attrs={"class":"form-control"}))
    birthday = forms.DateField(label="Birth", \
        widget=forms.DateInput(attrs={"class":"form-control"}))

