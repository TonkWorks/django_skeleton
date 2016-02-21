from __future__ import unicode_literals
from django.apps import AppConfig


class JobsConfig(AppConfig):
    name = "jobs"
    verbose_name = 'Jobs'

    def ready(self):
        from . import signals   # noqa
