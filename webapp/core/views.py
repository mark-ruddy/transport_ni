from django.shortcuts import render

from core.api_interact import get_soa_of_postcode
from .forms import PostCodeForm
from .api_interact import *

# Create your views here.

def index(request):
    form = PostCodeForm(request.POST)
    if form.is_valid():
        soa = get_soa_of_postcode(form.cleaned_data['postcode'])
        print(f"SOA: {soa}")

        # TODO: parse CSV here with that soa

        return render(request, 'index.html', {
            'form': form,
            'postcode_output': True,
            'postcode_formatted': "none",
        })
    else:
        form = PostCodeForm()

    return render(request, 'index.html', {
        'form': form,
    })

def contact(request):
    return render(request, 'contact.html', {})

def about_us(request):
    return render(request, 'about_us.html', {})
