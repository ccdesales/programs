import os.path

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.expanduser('~/PROGRAMS/django/inventario/inventory/inv/media'),
)

DB_NAME = os.path.expanduser("~/PROGRAMS/django/inventario/inventory/data/db.db3")

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.expanduser('~/PROGRAMS/django/inventario/templates'),
)
STATIC_ROOT = os.path.expanduser('~/PROGRAMS/django/media/')