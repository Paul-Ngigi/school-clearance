from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_first_name', 'user_last_name')
    search_fields = ['user__email', 'user__first_name', 'user__last_name']

    def user_email(self, obj):
        return obj.user.email

    def user_first_name(self, obj):
        return obj.user.first_name

    def user_last_name(self, obj):
        return obj.user.last_name

admin.site.register(Student, StudentAdmin)