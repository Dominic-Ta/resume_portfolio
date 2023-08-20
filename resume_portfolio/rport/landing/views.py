from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, JsonResponse
from django import forms
from django.shortcuts import render
import os
import environ
from django.middleware.csrf import rotate_token
import json

# from django.http import HttpResponse
# Create your views here.
# Create your views here.
# https://pypi.org/project/django-user-agents/
# if "iPhone" in request.META["HTTP_USER_AGENT"]:
#     user_agent = "iPhone"
# elif "MSIE" in request.META["HTTP_USER_AGENT"]:
#     user_agent = "MSIE"
# else:
#     user_agent = ""
# print(user_agent, "hello_world")
# print(request.META["HTTP_USER_AGENT"])
# print(request.headers["user-agent"])
# print(request.headers.get("user-agent"))
# if "Firefox" in request.headers.get("user-agent"):
#     print("hello there friend.")
# else:
#     print("you aren't a friend wtf.")
# return HttpResponse("Hello, world. You're at the polls index.")
# rotate_token(request)  # Generate a new CSRF token
def landing_view(request, *args, **kwargs):

    csrf_token = request.COOKIES.get('csrftoken')

    context = {
        'csrf_token': csrf_token
    }
    print(csrf_token)
    return render(request, "new_landing.html", context)
def privacy_view(request):
    return render(request, "privacy_policy.html")
def send_email_view(request,data):
    env = environ.Env()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    environ.Env.read_env(os.path.join(BASE_DIR, "rport/.env"))
    email_to = env("app_email")
    data = json.loads(data)
    if request.method == "POST":
        subject = data['Subject']
        contact_name = data['Contact_Name']
        contact_email = data['Contact_Email']
        message_to_send = data['Message']
        message = (
            "subject: "+ subject+ "\n"+ "message: "+ message_to_send+ "\nsent by: "+ contact_name+ "\ncontact email: "+ contact_email
        )
        send_mail(subject, message, contact_email, [email_to])
    else:
        return  JsonResponse({'message': 'Invalid Input'})
    return JsonResponse({'message': 'Email sent successfully.'})
