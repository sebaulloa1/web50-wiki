from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.get_title, name="title"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("wiki/<str:title>/edit/", views.edit_entry, name="edit_entry"),
    path("random_page/", views.random_page, name="random_page")
]
