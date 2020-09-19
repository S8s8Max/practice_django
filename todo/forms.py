from django import forms
from .models import Friend, Task

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ["name", "mail", "gender", "age", "birthday"]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mail': forms.EmailInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={"class":"form-control"}),
            "birthday":forms.DateInput(attrs={"class":"form-control"}),
        }

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

class FindForm(forms.Form):
    find = forms.CharField(label="Find", required=False, \
        widget=forms.TextInput(attrs={"class":"form-control"}))

class CheckForm(forms.Form):
    str = forms.CharField(label="Name",\
        widget=forms.TextInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data["str"]
        if (str.lower().startswith("no")):
            raise forms.ValidationError("You input 'NO'!")

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "content", "hitman"]
        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control \
                form-control-sm"}),
            "content": forms.Textarea(attrs={"class":"form-control \
                form-control-sm", "rows":2}),
            "hitman": forms.Select(attrs={"class":"form-control \
                form-control-sm"}),
        }

