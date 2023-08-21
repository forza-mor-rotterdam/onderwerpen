from apps.questions.models import Question
from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    ...


admin.site.register(Question, QuestionAdmin)
