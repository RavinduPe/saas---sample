from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings

from visits.models import PageVisit

LOGING_URL = settings.LOGIN_URL

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
VALID_CODE = "abc123"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    print(request.session.get('protected_page_allowed'), type(request.session.get('protected_page_allowed')))
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            request.session['protected_page_allowed'] = 1
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})


@login_required
def user_only_view(request, *args, **kwargs):
    return render(request, "protected/user_only.html", {})

@staff_member_required(login_url=LOGING_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request, "protected/staff_only.html", {})
    