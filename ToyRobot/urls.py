"""ToyRobot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from toyrobot_api import views
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robot/(?P<pk>.+)/(?P<move>.+)/',views.RobotDetail.as_view()),
    url(r'^robot/(?P<pk>.+)/$', views.RobotDetail.as_view()),
    url(r'^robot/$', views.RobotList.as_view()),
    url(r'^', views.RobotList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)