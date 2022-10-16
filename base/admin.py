from django.contrib import admin

# Register your models here.

from base.models import Project, Skill, Tag

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Tag)
