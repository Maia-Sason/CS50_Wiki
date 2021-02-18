from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title of Entry")
    body = forms.CharField(widget=forms.Textarea(attrs={"style":"height:30em;"}))

def index(request):
    if request.method == "POST":

        result = request.POST["q"]
        if util.get_entry(result) == None:
            result_list = util.query(result)
            return render(request, "encyclopedia/index.html", {
                "entries" : result_list
            })
        else:
            return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={'title': result}))
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def wiki(request, title):
    return render(request, "encyclopedia/wiki.html", {
        "title": util.get_entry(title.upper())
    })

def new(request):
    ''' render new.html '''
    if request.method == "POST":
        ''' do something '''
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            print(title)
            body = form.cleaned_data["body"]
            if util.get_entry(title) != None:
                return HttpResponse("Sorry, Entry under this title already exists!")
            util.save_entry(title, body)
            return HttpResponseRedirect(reverse("encyclopedia:wiki", kwargs={'title': title}))


    edit = None
    return render(request, "encyclopedia/new.html", {
        "edit": edit,
        "form": NewEntryForm()
    })
    

def edit(request, title):
    ''' render edit or just pass args to new.html '''
    if request.method == "POST":
        ''' do something '''

    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm(),
        "edit": util.get_entry(title)
    })

def random(request):
    ''' function that pulls a random entry and passes into
        wiki'''

def search(request):
    ''' function that returns list of entries
        that match with request or 1 entry or none '''
    return HttpResponse("ugui")
