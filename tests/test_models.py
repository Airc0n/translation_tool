from django.test import TestCase
# Create your tests here.
from django.utils import timezone

from translation_tool.forms import TemplateResourceForm
from translation_tool.models import HtmlTemplate, TemplateResource
from translation_tool.tests.libs import create_user


class HtmlTemplateTestCase(TestCase):

    def test_capture_resource_from_html(self):
        assert 1 == 1


class TemplateResourceTestCase(TestCase):
    def setUp(self) -> None:
        self.user = create_user()
        now_time = timezone.now()
        self.template = HtmlTemplate.objects.create(name="test",
                                                    html="""<div class="{{ headline_class}}">
                                            {{ headline }}
                                            </div>""",
                                                    created_at=now_time,
                                                    modified_at=now_time,
                                                    created_by=self.user,
                                                    modified_by=self.user
                                                    )

    def test_form_save(self):
        now_time = timezone.now()
        f = TemplateResourceForm.AdminPanelEditForm({
            'html_template': self.template,
            'data': {
                'headline_class': 'test',
                'test': '123'
            },
            'locale': 'en_us',
            'create_at': now_time,
            'modified_at': now_time,
            'create_by_id': self.user.id,
            'modified_by_id': self.user.id,
        })
        
        f.save()
        
        # TemplateResource.objects.create(html_template=self.template,
        #                                 locale="en_us",
        #                                 data={
        #
        #                                 },
        #                                 created_at=now_time,
        #                                 modified_at=now_time,
        #                                 created_by=self.user,
        #                                 modified_by=self.user
        #                                 )
