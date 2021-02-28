from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings
from django.utils.translation import ugettext as _
from djangocms_rawhtml.models import RawHTMLPluginData

@plugin_pool.register_plugin
class RawHTMLPluginPublisher(CMSPluginBase):
    """
    Plugin to manage raw HTML text that needs to be managed from the admin interface.
    """
    name = _("Raw HTML")
    model = RawHTMLPluginData
    change_form_template = "admin/djangocms_rawhtml/change_form.html"
    render_template = "djangocms_rawhtml/plugins/raw.html"
    allow_children = False
    
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        """
        If we've set a theme setting, pass that along.
        """
        if hasattr(settings, 'CODEMIRROR_THEME'):
            theme = settings.CODEMIRROR_THEME
        else:
            theme = None

        context.update({
            'theme': theme
        })

        return super().render_change_form(request, context, add, change, form_url, obj)
