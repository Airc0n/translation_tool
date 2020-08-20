import re

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.exceptions import ValidationError
from django.db import models


class CoreModel(models.Model):
    """translation tool's core model fields"""
    vhost = models.CharField(
        verbose_name='target vhost',
        max_length=255,
        default='',
    )

    created_at = models.DateTimeField(
        verbose_name='created at',
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        verbose_name='created by',
        to=settings.AUTH_USER_MODEL,
        related_name='created_%(class)s_set',
    )
    modified_at = models.DateTimeField(
        verbose_name='modified at',
        auto_now=True,
    )
    modified_by = models.ForeignKey(
        verbose_name='modified by',
        to=settings.AUTH_USER_MODEL,
        related_name='modified_%(class)s_set',
    )

    class Meta:
        abstract = True


class HtmlTemplate(CoreModel):
    """
    Record frontend developer input html templates
    and extract template key and value.
    """
    name = models.CharField(max_length=255, help_text="give a naming to this template", verbose_name="template name")
    html = models.TextField(help_text="input html template here...")

    def __str__(self):
        return self.name


class TemplateResource(CoreModel):
    """
    Resources data
    """
    html_template = models.ForeignKey(HtmlTemplate)
    locale = models.CharField(max_length=10, help_text="format =>  {language_code}_{country_code} ")
    data = JSONField(default=dict())

    def __str__(self):
        return self.locale

    class Meta:
        unique_together = ("html_template", "locale",)

    def clean(self):
        # verify template key/value number amount match user input data key/value
        """ verify locale format """
        pattern = re.compile(r'^[a-z]{2,3}_([a-zA-Z]{2})?$')
        results = pattern.findall(self.locale)
        if not results or len(results) == 0:
            raise ValidationError('locale format error...')

        # # find keys from user select template
        # pattern = re.compile(r'{{\s*(\w+)\s*}}')
        # results = pattern.findall(self.html_template.html)
        #
        # if not results or len(results) == 0:
        #     raise ValidationError('You select template has no keys, please contact frontend engineer...')
        #
        # template_keys = dict.fromkeys(results)
        # keys_diff = template_keys.keys() - self.data.keys()
        # if len(keys_diff) > 0:
        #     raise ValidationError('Your resource data lack of keys: %s' % ','.join(keys_diff))
