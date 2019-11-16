from django.contrib import admin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','name', 'student_number', 'major','grade')
    list_display_links = ('id', 'name')