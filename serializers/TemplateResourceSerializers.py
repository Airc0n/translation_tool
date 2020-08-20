from translation_tool.models import TemplateResource
from translation_tool.serializers.BaseSerializers import BaseSerializers


class ListSerializers(BaseSerializers):
    class Meta:
        model = TemplateResource
        fields = ("id", "locale", "data", "modified_by", "modified_at")
