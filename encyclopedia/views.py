from django.shortcuts import render, redirect
import markdown2
from . import util
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_title(request, title):
    try:
        page_title = util.get_entry(title)
        page_content = markdown2.markdown(page_title)
        return render(request, "encyclopedia/title.html", {
            "page_content": page_content,
            "page_title": title
        })
    except TypeError:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

def search(request):
        title = request.POST["title"]
        page_title = util.get_entry(title)
        if page_title == None:
            entries = util.list_entries()
            sub_entries = []
            for entry in entries:
                if title in entry.lower():
                    sub_entries.append(entry)
            if not sub_entries:
                return render(request, "encyclopedia/error.html", {
                    "title": title
                })
            else:
                return render(request, "encyclopedia/search.html", {
                    "entries": sub_entries
                })
        else:
            return redirect('title', title=title)



def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST["title"]
        entries = util.list_entries()
        for entry in entries:
            if title == entry.lower():
                return render(request, "encyclopedia/error.html", {
                    "existing_title": title.capitalize()
                })
        util.save_entry(title, request.POST["entry_text"])
        return redirect('title', title=title)


def edit_entry(request, title):
    if request.method == "GET":
        entry = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "page_content": entry
        })
    else:
        util.save_entry(title, request.POST["entry_text"])
        return redirect('title', title=title)

def random_page(request):
    entries = util.list_entries()
    return redirect('title', title=random.choice(entries))
