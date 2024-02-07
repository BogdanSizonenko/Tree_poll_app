from django.contrib import admin

from django_mptt_admin.admin import DjangoMpttAdmin

from .models import Test, Question, Choice


admin.site.site_header = "Админ панель"


class TestAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date")
    
    
admin.site.register(Test, TestAdmin)

    
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(DjangoMpttAdmin):
    list_display = ("test", "question_text", "parent", "choice_trigger", "display")
    inlines = [ChoiceInLine]
 
 
admin.site.register(Question, QuestionAdmin)