from django.contrib import admin

from task.models import Task


# add the Task model for the admin interface
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'completed')
    list_display_links = ('id', )
    list_editable = ('title', 'author', 'completed')
    search_fields = ('title', 'author')

    # fieldsets for the 'add' form for a new team
    add_fieldsets = (
        ('Team', {'fields': ('title', 'author')}),
        ('Info', {'fields': ('description', 'completed')})
    )

    # fieldsets for the 'add' form for a new team
    fieldsets = (
        ('Team', {'fields': ('title', 'author')}),
        ('Info', {'fields': ('description', 'completed')})
    )
