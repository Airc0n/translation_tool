from bs4 import BeautifulSoup
from rest_framework import serializers
from translation_tool.models import HtmlTemplate
from translation_tool.serializers.BaseSerializers import BaseSerializers


class ListSerializers(BaseSerializers):
    class Meta:
        model = HtmlTemplate
        fields = ("id", "name", "html", "modified_by", "modified_at")
