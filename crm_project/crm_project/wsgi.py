"""
WSGI config for crm_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from payments.cron import remainder_mail

remainder_mail()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')

application = get_wsgi_application()
