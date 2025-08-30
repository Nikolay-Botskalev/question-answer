from django.contrib import admin

from application.models.question import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_editable = ('text',)
    ordering = ('-create_at',)
    search_fields = ('text__startswith',)
    fields = ('text',)
