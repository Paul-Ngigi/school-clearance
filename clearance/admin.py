from django.contrib import admin
from .models import Clearance, Review

# Register your models here.
class ClearanceAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'user_first_name', 'user_last_name', 'status', 'completed', 'initiated_at')
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'status', 'completed',]

    def user_email(self, obj):
        return obj.student.user.email

    def user_first_name(self, obj):
        return obj.student.user.first_name

    def user_last_name(self, obj):
        return obj.student.user.last_name

class ReviewAdmin(admin.ModelAdmin):    
    list_display = ('user_email', 'user_first_name', 'user_last_name', 'status', 'completed', 'initiated_at')
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'status', 'completed',]

    def user_email(self, obj):
        return obj.student.user.email

    def user_first_name(self, obj):
        return obj.student.user.first_name

    def user_last_name(self, obj):
        return obj.student.user.last_name

admin.site.register(Clearance, ClearanceAdmin)
admin.site.register(Review)