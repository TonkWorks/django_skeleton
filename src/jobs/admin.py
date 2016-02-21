from __future__ import unicode_literals
from django.contrib import admin
from authtools.admin import NamedUserAdmin
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from .models import Job
from .models import Event
from .crunchbase_models import Company


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title', 'description']
    date_hierarchy = 'pub_date'

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date',)
    list_filter = ['date']
    search_fields = ['title', 'description']
    date_hierarchy = 'date'

class CompanyAdmin(admin.ModelAdmin):
    list_display = Company._meta.get_all_field_names()

    list_filter = ['last_funding_at']
    search_fields = ['name', 'homepage_url']
    date_hierarchy = 'last_funding_at'


admin.site.register(Job, JobAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Company, CompanyAdmin)
