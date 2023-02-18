from django.shortcuts import render
from .postcode import Postcode
from .forms import PostCodeForm

# Create your views here.

def index(request):
    form = PostCodeForm(request.POST)
    if form.is_valid():
        postcode = Postcode()
        postcode.format_postcode(form.cleaned_data['postcode'])
        return render(request, 'index.html', {
            'form': form,
            'postcode_output': True,
            'postcode_formatted': postcode.formatted_postcode,
        })
    else:
        form = PostCodeForm()

    return render(request, 'index.html', {
        'form': form,
    })
