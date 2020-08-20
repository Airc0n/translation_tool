from django import forms
from translation_tool.models import HtmlTemplate


class AdminPanelEditForm(forms.ModelForm):
    class Meta:
        model = HtmlTemplate
        fields = ("name", "html",)
