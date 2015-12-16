from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template

def histogram(request,f):
    template = get_template(f)
    rendz = template.render()
    counts = {}
    for word in rendz:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    template_markup = Template('<html><body> Name : {{filename}} Words: <ul>{%for key,value in dic%} <li> {{key}}   {{value}}</li>{%endfor%} </ul></body></html>')
    html = temp.render(Context({'filename':f,'dic':counts}))
    return HttpResponse(html)


