from django.shortcuts import render
from .forms import PostCodeForm

# Create your views here.

def index(request):
    form = PostCodeForm(request.POST)
    if form.is_valid():
        pass
        # TODO: process the address and display result back to user
    else:
        form = PostCodeForm()

    return render(request, 'index.html', {
        'form': form,
        'test_data': 'some test data'
    })
