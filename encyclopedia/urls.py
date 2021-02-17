from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("random", views.random, name="random"),
    path("new", views.new, name="new"),
    path("edit", views.edit, name="edit")
]
