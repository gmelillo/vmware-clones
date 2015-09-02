__author__ = 'gabriel'

from pkg_resources import resource_filename
from sys import prefix

EMAIL_TEMPLATE = '{0}/{1}'.format(
    prefix,
    resource_filename(__name__, 'email_notification.html')
)

from jinja2 import Template


def get_email_notification_template():
    return Template(
        open(EMAIL_TEMPLATE, 'r+').read()
    )