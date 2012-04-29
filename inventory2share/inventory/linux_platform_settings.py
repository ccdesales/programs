import os.path

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.expanduser('~/REPO/GIT/inventory/inventory/inv/media'),
)

DB_NAME = os.path.expanduser("~/REPO/GIT/inventory/inventory/data/db.db3")

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.expanduser('~/REPO/GIT/inventory/templates'),
)
STATIC_ROOT = os.path.expanduser('~/REPO/GIT/inventory/media/')