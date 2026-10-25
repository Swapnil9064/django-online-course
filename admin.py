from django.contrib import admin
from .models import Course,Lesson,Question,Choice,Submission
class ChoiceInline(admin.TabularInline):
 model=Choice; extra=2
class QuestionInline(admin.StackedInline):
 model=Question; extra=1
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
 list_display=('id','name'); search_fields=('name',)
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
 list_display=('id','question_text','course'); inlines=[ChoiceInline]
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
 list_display=('id','title','course')
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
 list_display=('id','choice_text','question','is_correct')
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
 list_display=('id','user','course','score','total_questions','submitted_at')
