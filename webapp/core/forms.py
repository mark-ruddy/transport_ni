from django import forms

class PostCodeForm(forms.Form):
    postcode = forms.CharField(label="Enter Postcode", max_length=7, min_length=5, widget=forms.TextInput(attrs={"class": "form-control"}))
