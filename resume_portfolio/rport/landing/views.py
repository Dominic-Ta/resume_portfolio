from django.shortcuts import render


# from django.http import HttpResponse
# Create your views here.
# Create your views here.
# https://pypi.org/project/django-user-agents/
def landing_view(request, *args, **kwargs):
    if "iPhone" in request.META["HTTP_USER_AGENT"]:
        user_agent = "iPhone"
    elif "MSIE" in request.META["HTTP_USER_AGENT"]:
        user_agent = "MSIE"
    else:
        user_agent = ""
    print(user_agent, "hello_world")
    print(request.META["HTTP_USER_AGENT"])
    print(request.headers["user-agent"])
    print(request.headers.get("user-agent"))
    if "Firefox" in request.headers.get("user-agent"):
        print("hello there friend.")
    else:
        print("you aren't a friend wtf.")
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "landing.html")

