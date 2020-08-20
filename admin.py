from django.contrib import admin
from django.utils import timezone
from django.utils.functional import curry
from django.utils.html import format_html

from translation_tool import models
from translation_tool.forms import HTMLTemplateForm, TemplateResourceForm
from translation_tool.models import TemplateResource


class CoreAdminPanel(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.select_related("modified_by")
        return qs

    def save_model(self, request, obj: models.CoreModel, form, change):
        user = request.user
        now_time = timezone.now()
        if not obj.created_by_id:
            obj.created_by = user
            obj.created_at = now_time

        obj.modified_by = user
        obj.modified_at = now_time

        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        print('called...', change)
        instances = formset.save(commit=False)

        user = request.user
        now_time = timezone.now()

        for instance in instances:
            if not instance.created_by_id:
                instance.created_by = user
                instance.created_at = now_time

            instance.modified_by = user
            instance.modified_at = now_time
            instance.save()
        formset.save_m2m()


class TemplateResourceInline(admin.StackedInline):
    model = TemplateResource
    fk_name = "html_template"
    verbose_name = "resource"
    extra = 0
    fieldsets = (
        (None, {
            'fields': (
                'locale',
                'data',
                'generate_html_button'
            )
        }),
    )
    readonly_fields = ("generate_html_button",)

    def generate_html_button(self, obj):
        # print('template:', obj.html_template.html)
        # print('resource:', obj.data)
        ####

        return format_html('<a class="grp-button grp-default" href="#">Generate HTML and Copy it</a>')

    generate_html_button.allow_tags = True


@admin.register(models.HtmlTemplate)
class HTMLTemplateAdminPanel(CoreAdminPanel):
    form = HTMLTemplateForm.AdminPanelEditForm
    search_fields = ("name", "html",)
    list_display = ("name", "html", "modified_by", "modified_at")
    inlines = (TemplateResourceInline,)


@admin.register(models.TemplateResource)
class TemplateResourceAdminPanel(CoreAdminPanel):
    form = TemplateResourceForm.AdminPanelEditForm
    search_fields = ("locale", "html_template__name",)
    list_display = ("html_template", "locale", "modified_by", "modified_at")
