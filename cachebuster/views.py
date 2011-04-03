__author__ = 'jaddison'

"""
Views and functions for serving static files. These are only to be used during
development, and SHOULD NOT be used in a production setting.
"""
from django.conf import settings
from django.http import Http404
from django.contrib.staticfiles.views import serve as django_staticfiles_serve
from django.views.static import serve as django_serve


def static_serve(request, path, document_root=None, insecure=False, **kwargs):
    try:
        return django_staticfiles_serve(request, path, document_root, insecure, **kwargs)
    except Http404:
        if getattr(settings, 'CACHEBUSTER_PREPEND', False):
            unique_string, new_path = path.split("/", 1)
            return django_staticfiles_serve(request, new_path, document_root, insecure, **kwargs)
        raise


def media_serve(request, path, document_root=None, show_indexes=False):
    try:
        return django_serve(request, path, document_root, show_indexes)
    except Http404:
        if getattr(settings, 'CACHEBUSTER_PREPEND', False):
            unique_string, new_path = path.split("/", 1)
            return django_serve(request, new_path, document_root, show_indexes)
        raise
