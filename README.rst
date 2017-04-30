djangcms-rawhtml
================

DjangoCMS Plugin that lets you insert raw HTML code into a page.

This idea might seem offensive to some CMS "purists", but every now and then there are times when inserting a little block of HTML code is needed to get a job done quickly.

This Plugin combines the ideas of `cmsplugin-raw-html <https://github.com/makukha/cmsplugin-raw-html>`_
with `code-editor-django-admin <https://mr-coffee.net/blog/code-editor-django-admin>`_ by giving 
you a nice HTML editor `CodeMirror <http://codemirror.net/>`_ to edit the code in rather than 
a default ``TextField``.

Installation
------------

1. Add to your ``INSTALLED_APPS`` (in ``settings.py``):

    INSTALLED_APPS = (
        ...
        'djangocms-rawhtml',
        ...
    )

2. Run migrations:

    python manage.py migrate djangocms_rawhtml

3. "Raw HTML" should now be available as a plugin in the CMS!