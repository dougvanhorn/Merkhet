# Keep your imports at the top of the module.  When you hit a circular import
# move them into the function or method where they're needed.
#
# Also, keep them sorted and organized.
#
# And read PEP-8: http://legacy.python.org/dev/peps/pep-0008/

from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User

from . import models


@admin.register(models.HourEntry)
class HourEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'task', 'notes', 'pub_date', 'hours',
                    'cost', 'billable', 'billed')


admin.site.register(models.Project)
admin.site.register(models.Task)

