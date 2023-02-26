from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Todos

# Create your views here.

def index(request):
    mytodo = Todos.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mytodo': mytodo,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['item']
    todo = Todos(item=x)
    todo.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    todo = Todos.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))


def update(request, id):
    mytodo = Todos.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mytodo' : mytodo,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    item = request.POST['item']
    todo = Todos.objects.get(id=id)
    todo.item = item
    todo.save()
    return HttpResponseRedirect(reverse('index'))
    