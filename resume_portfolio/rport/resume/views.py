from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.shortcuts import render, redirect
import boto3
import os
import environ

import warnings

warnings.filterwarnings("ignore")
# from django.http import HttpResponse


def link_to_resume(request):
    """
    PythonDeprecationWarning: Boto3 will no longer support Python 3.5
    starting February 1, 2021. To continue receiving service updates,
    bug fixes, and security updates please upgrade to Python 3.6 or later.
    More information can be found here:
    https://aws.amazon.com/blogs/developer/announcing-the-end-of-support-for-python-3-4-and-3-5-in-the-aws-sdk-for-python-and-aws-cli-v1/
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env = environ.Env()
    environ.Env.read_env(os.path.join(BASE_DIR, "rport/.env"))

    s3 = boto3.client(
        "s3",
        aws_access_key_id=env("aws_access_key_id"),
        aws_secret_access_key=env("aws_secret_access_key"),
    )
    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": env("bucket_name"), "Key": env("f_name")},
        ExpiresIn=600,
    )
    return HttpResponseRedirect(url)


class send_the_email(forms.Form):
    contact_name = forms.CharField(max_length=35, label="Name")
    contact_email = forms.EmailField()
    Subject = forms.CharField(max_length=35, label="Subject")
    contact_Message = forms.CharField(
        widget=forms.Textarea(attrs={"cols": "50", "rows": "15"}), label="Message"
    )


def email(request):
    env = environ.Env()
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    environ.Env.read_env(os.path.join(BASE_DIR, "rport/.env"))
    email_to = env("app_email")
    if request.method == "GET":
        form = send_the_email()
    else:
        form = send_the_email(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["Subject"]
            from_email = form.cleaned_data["contact_email"]
            message = (
                "subject: "
                + subject
                + "\n"
                + "message: "
                + form.cleaned_data["contact_Message"]
                + "\nsent by: "
                + form.cleaned_data["contact_name"]
                + "\ncontact email: "
                + form.cleaned_data["contact_email"]
            )
            print(message)
            try:
                send_mail(subject, message, from_email, [email_to])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("resume")
    return render(request, "send_email.html", {"form": form})


def thanks(request):
    return HttpResponse("Thank you for your message.")
