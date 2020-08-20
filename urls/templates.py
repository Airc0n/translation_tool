"""
URL patterns for translation related templates.
"""
from django.conf.urls import url

from translation_tool.views import template_views

urlpatterns = [
    url(r'^template/$', template_views.TemplateListView.as_view(), name="template_list"),
    url(r'^template/html/$', template_views.GeneratePureHtmlView.as_view(),
        name="pure_html_view"),
]
