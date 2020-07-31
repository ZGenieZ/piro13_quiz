from django.contrib import admin
from .models import Quiz, Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline, ]



admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)

#admin.site.register(Quiz)
#admin.site.register(Question)
#admin.site.register(Choice)



