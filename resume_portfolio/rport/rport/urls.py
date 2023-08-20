"""test_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from resume.views import email, link_to_resume
from api import views
from django.urls import path, include
from rest_framework import routers
from landing.views import landing_view, privacy_view, send_email_view
from examples.views import main_view, table_load, load_map
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# path("resume/", home_view, name="resume"),
urlpatterns = [
    path("", landing_view, name="home"),
    path("privacy_policy", privacy_view, name="privacy_policy"),
    path("resume", email, name="resume"),
    path("resume/url", link_to_resume, name="resume_url"),
    path("api/", include("api.urls"), name="api"),
    path("examples/", include("examples.urls")),
    path('send-email/<str:data>', send_email_view, name='send_email'),
]
