from django.contrib import admin
from Quiz.models import Quiz

class QuizAdmin(admin.ModelAdmin):
    list_display=['name','price','image']

# Register your models here.
admin.site.register(Quiz,QuizAdmin)
