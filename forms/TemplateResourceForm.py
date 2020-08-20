from django import forms
from translation_tool.models import TemplateResource


class AdminPanelEditForm(forms.ModelForm):
    class Meta:
        model = TemplateResource
        fields = ("html_template", "locale", "data")
