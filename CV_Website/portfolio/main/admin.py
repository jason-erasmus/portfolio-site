from django.contrib import admin

from .models import Project, ProjectImage, Tag


# edit models at same time instead of separately
class ProjectImageInline(admin.TabularInline):
    # The code snippet `model = ProjectImage` inside the `ProjectImageInline` class
    # is specifying the model that the inline formset should be based on. In this
    # case, it is indicating that the inline formset should be based on the
    # `ProjectImage` model.
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    # The code snippet you provided is configuring the Django admin interface for the
    # `Project` model. Here's what each line is doing:
    list_display = ("title", "link")
    inlines = [ProjectImageInline]
    search_fields = ("title", "description")
    list_filter = ("tags",)


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
