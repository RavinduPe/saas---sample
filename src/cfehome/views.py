from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    PageVisit.objects.create(path=request.path)
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    page_visit_count = page_qs.count()
    total_visit_count = qs.count()
    # print("path", request.path)
    return render(request, "home.html", {"title": "Home Page", "content": "Welcome to the home page.",
                                         "queryset":qs,
                                         "page_visit_count":page_visit_count,
                                         "Total_visit_count" : total_visit_count,
                                         })

def about_view(request, *args, **kwargs):
    print(request.user.is_authenticated, request.user)
    PageVisit.objects.create(path=request.path)
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    page_visit_count = page_qs.count()
    total_visit_count = qs.count()
    try:
        presentage = (page_visit_count / total_visit_count) * 100
    except:
        presentage = 0
    return render(request, "about.html", {"title": "About Page", 
                            "content": "Welcome to the about page.", "page_visit_count": page_visit_count, 
                            "total_visit_count": total_visit_count, "presentage": presentage})

def old_home_page_view(request, *args, **kwargs):
    my_title = "Hello World!"
    my_context = {
        "title":"Hello World!",
        "content":"Welcome to the home page.",
    }
    html = """
    <DOCTYPE html>
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h1>{title}</h1>
            <p>{content}</p>
        </body>
    </html>"""
    return HttpResponse(html.format(**my_context))