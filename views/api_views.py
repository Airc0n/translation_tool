from django.core.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from translation_tool.models import HtmlTemplate, TemplateResource
from translation_tool.serializers import HTMLTemplateSerializers, TemplateResourceSerializers


class HTMLTemplateList(ListAPIView):
    """ List all html template """
    queryset = HtmlTemplate.objects.all()
    serializer_class = HTMLTemplateSerializers.ListSerializers
    # permission_classes = [IsAdminUser]


class TemplateResourceList(ListAPIView):
    """ List belong the html_template resources """
    serializer_class = TemplateResourceSerializers.ListSerializers

    def get_queryset(self):
        """ query by template id, otherwise, raise exception..."""
        template_id = self.request.GET.get('tid', None)
        if not template_id:
            raise Exception("You didn't given tid parameter...")

        return TemplateResource.objects.filter(html_template_id=template_id)


