from django import forms

OPEN_SOURCE_FILE_HINT = "Github, Gitlab, or any URL link to source code file"

class PostCodeForm(forms.Form):
    address = forms.CharField(label="Enter Postcode", max_length=9, min_length=9, widget=forms.TextInput(attrs={"class": "form-control"}))
