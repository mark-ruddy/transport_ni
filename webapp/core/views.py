from django.shortcuts import render
from .forms import AddressForm

# Create your views here.

def index(request):
    form = AddressForm(request.POST)
    if form.is_valid():
        pass
        # TODO: process the address and display result back to user
    else:
        form = AddressForm()

    return render(request, 'index.html', {
        'test_data': 'some test data'
    })
