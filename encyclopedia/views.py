from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
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