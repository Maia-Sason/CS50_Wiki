from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from . import util

class NewSearchForm(forms.Form):
    searches = forms.CharField(label="q")


def index(request):
    if request.method == "POST":
        form = NewSearchForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data["searches"]
            print(result)
            
            return HttpResponseRedirect(reverse("encyclopedia:search"))
        else:
            print("HEEELP")
            return HttpResponse("Hello, world...")

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : NewSearchForm()
    })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "title": util.get_entry(title.upper())
    })

def new(request):
    ''' render new.html '''

def edit(request):
    ''' render edit or just pass args to new.html '''

def random(request):
    ''' function that pulls a random entry and passes into
        wiki'''

def search(request):
    ''' function that returns list of entries
        that match with request or 1 entry or none '''
    return HttpResponse("ugui")
