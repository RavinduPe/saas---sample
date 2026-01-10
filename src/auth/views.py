from django.contrib.auth import authenticate, login
from django.shortcuts import render , redirect

def login_view(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None
        if all([username,password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Logged in successfully")
                return redirect('/')
                # Redirect to a success page.
                ...
            else:
                # Return an 'invalid login' error message.
                ...
    return render(request, "auth/login.html", {"title": "Login"})

# def register_view(request, *args, **kwargs):
#     return render(request, "auth/register.html", {"title": "Register"})