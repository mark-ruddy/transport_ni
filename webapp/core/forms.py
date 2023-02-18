from django import forms

OPEN_SOURCE_FILE_HINT = "Github, Gitlab, or any URL link to source code file"

class PostCodeForm(forms.Form):
    postcode = forms.CharField(label="Enter Postcode", max_length=7, min_length=7, widget=forms.TextInput(attrs={"class": "form-control"}))
