from django.db import models
from six import python_2_unicode_compatible
from cms.models.pluginmodel import CMSPlugin
from django.utils.text import Truncator
from django.utils.html import strip_tags


@python_2_unicode_compatible
class RawHTMLPluginData(CMSPlugin):
    """
    Model for Raw HTML Plugin
    
    body - contains the HTML source text
    label - used for display purposes on the admin site
    """

    label = models.CharField(max_length=40, default="")
    body = models.TextField('HTML')

    def __str__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")
    def __unicode__(self):
        return Truncator(strip_tags(self.label).replace('&shy;', '')).words(5, truncate="...")
