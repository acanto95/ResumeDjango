# api/urls.py
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^maininfo/$', views.MainInfoList.as_view()),
    url(r'^experienceinfo/$', views.ExperienceInfoList.as_view()),
    url(r'^skillsinfo/$', views.SkillsInfoList.as_view()),
    url(r'^proyectsinfo/$', views.ProyectsInfoList.as_view()),
    url(r'^comments/$', views.CommentsList.as_view()),
   	url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentsDetail.as_view()),
]