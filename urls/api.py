"""
URL patterns for translation related templates.
"""
from django.conf.urls import url
from translation_tool.views import api_views

urlpatterns = [
    url(r'^v1/translation/templates/$', api_views.HTMLTemplateList.as_view()),
    url(r'^v1/translation/resources/$', api_views.TemplateResourceList.as_view()),
]
