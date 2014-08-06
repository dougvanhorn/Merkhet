from django.contrib import admin

from Merkhet.models import HourEntry
class HourEntryAdmin(admin.ModelAdmin):
    list_display = ('project','name','task','notes','pub_date','hours', 'cost','billable','billed')

admin.site.register(HourEntry, HourEntryAdmin)

from Merkhet.models import Project
admin.site.register(Project)

from Merkhet.models import Task
admin.site.register(Task)

from django.contrib.admin import AdminSite
