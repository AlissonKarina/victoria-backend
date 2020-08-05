from django.contrib import admin

from .models import AnswerQuestion, Paper, AnswerText, Question, Parameter
# Register your models here.

class PaperAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'created', 'updated')

admin.site.register(AnswerQuestion)
admin.site.register(Paper, PaperAdmin)
admin.site.register(AnswerText)
admin.site.register(Question)
admin.site.register(Parameter)
