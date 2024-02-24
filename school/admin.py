from django.contrib import admin
from school.models import Student, Course

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code', 'desc')
    list_display_links = ('id', 'code')
    search_fields = ('code',)

admin.site.register(Course, Courses)
