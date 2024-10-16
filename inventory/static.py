from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.utils import get_dirs
import os

# Collect static files here
__all__ = []

def get_static_dirs(parent=None):
    if parent is None:
        parent = os.path.dirname(__file__)

    static_dir = os.path.join(parent, 'static')
    return (os.path.join(parent, static_dir),)

def get_static_files(parent=None):
    return get_files(get_static_dirs(parent), '')
