from chevron.tokenizer import tokenize
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.base import View

from translation_tool.models import TemplateResource


class TemplateListView(TemplateView):
    """ render template list """
    template_name = 'translation_tool/template_list.html'


class GeneratePureHtmlView(View):
    """ render pure html by template and resource """

    def get(self, request, *args, **kwargs):
        rid = request.GET.get('rid', False)  # resource id
        resource = TemplateResource.objects.select_related("html_template").get(pk=rid)

        import chevron
        structure = {}
        is_tag_open=False
        for tag_type, tag_key in tokenize(resource.html_template.html):
            # if t[0] in ['variable', 'section']:
            if is_tag_open:
                pass
            else:
                if tag_type == 'variable':
                    structure[tag_key] = {}
                elif tag_type == 'section':
                    is_tag_open=True
                    structure[tag_key] = list()

            print('structure:', structure)

        output = chevron.render(resource.html_template.html, resource.data)

        return HttpResponse(output, content_type='text/plain')
