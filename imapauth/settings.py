from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

IMAPAUTH_HOST = getattr(settings, 'IMAPAUTH_HOST', None)

if IMAPAUTH_HOST is None:
    raise ImproperlyConfigured("In order to use django-imapauth "
        "you have to configure IMAPAUTH_HOST at your settings module")
