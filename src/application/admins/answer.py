from django.contrib import admin

from application.models.answer import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'user_id')
    list_editable = ('text', 'question')
    ordering = ('-create_at',)
    search_fields = ('text__startswith', 'user_id')
    fields = ('text', 'question', 'user_id')
