from django.shortcuts import render
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_title(request, title):
    try:
        page_title = util.get_entry(title)
        print(page_title)
        page_content = markdown2.markdown(page_title)
        print(page_content)
        return render(request, "encyclopedia/title.html", {
            "page_content": page_content
        })
    except TypeError:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

def search(request):
    if request.method == "POST":
        title = request.form.get("title")
        try:
            page_title = util.get_entry(title)
            page_content = markdown2.markdown(page_title)
            return render(request, "encyclopedia/title.html", {
                "page_content": page_content
            })
        except ValueError:
            return render(request, "encyclopeida/index.html")

            """
        except TypeError:
            entries = util.list_entries()
            print(entries, "entries")
            sub_entries = {}
            for entry in entries:
                if title in entry:
                    sub_entries.append(entry)
            print(sub_entries, "sub")
            if not sub_entries:
                return render(request, "encyclopedia/error.html", {
                    "title": title
                })
            else:
                return render(request, "encyclopedia/search.html", {
                    "entries": sub_entries
                })
        """