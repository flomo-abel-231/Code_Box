from django.contrib import admin

# Register your models here.

from . models import Standard,Lesson,WorkingDays,Subject

# Register your models here.
admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(WorkingDays)