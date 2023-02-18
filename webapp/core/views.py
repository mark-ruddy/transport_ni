from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    # template = loader.get_template('templates/index.html')
    # latest_question_list = ["first", "second"]
    # context = {
    #        'latest_question_list': latest_question_list,
    #    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', {
        'test_data': 'some test data'
    })
