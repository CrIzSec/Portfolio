from django.contrib import admin
from .models import Project, Image

class ProjectImageAdmin(admin.StackedInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
