from django.shortcuts import render

from .forms import PostCodeForm
from .api_interact import *
from .parse_csv import *

# Create your views here.

def index(request):
    form = PostCodeForm(request.POST)
    if form.is_valid():
        resp_json = query_postcode(form.cleaned_data['postcode'])
        soa = get_soa_from_resp_json(resp_json)
        soa_row = parse_soa_vacancies(soa)
        soa_jobs = soa_row[1]
        print(f"SOA: {soa_row}")
        lon = get_lon_from_resp_json(resp_json)
        print(f"Longitude: {lon}")

        return render(request, 'index.html', {
            'form': form,
            'postcode_output': True,
            'postcode': form.cleaned_data['postcode'],
            'soa': soa,
            'soa_jobs': soa_jobs,
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
