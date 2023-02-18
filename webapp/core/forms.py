from django import forms

OPEN_SOURCE_FILE_HINT = "Github, Gitlab, or any URL link to source code file"

class AddressForm(forms.Form):
    address = forms.CharField(label="Your Address", max_length=9, min_length=9, widget=forms.TextInput(attrs={"placeholder": "Address", "class": "form-control"}))
