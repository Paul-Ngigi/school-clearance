from django.contrib import admin
from .models import Clearance, Review

# Register your models here.
class ClearanceAdmin(admin.ModelAdmin):
    list_display = ('student_email', 'student_first_name', 'student_last_name', 'status', 'completed', 'initiated_at')
    search_fields = ['student__email', 'student__first_name', 'student__last_name', 'status', 'completed',]

    def student_email(self, obj):
        return obj.student.user.email

    def student_first_name(self, obj):
        return obj.student.user.first_name

    def student_last_name(self, obj):
        return obj.student.user.last_name

class ReviewAdmin(admin.ModelAdmin):    
    list_display = ('student_email', 'reviewer_email', 'reviewer_role', 'approved', 'rejected', 'created_at')
    search_fields = ['student__email', 'reviewer_email', 'reviewer_role', 'approved', 'approved', 'rejected']

    def student_email(self, obj):
        return obj.clearance.student.user.email

    def reviewer_email(self, obj):
        return obj.reviewer.email

    def reviewer_role(self, obj):
        return obj.reviewer.role

admin.site.register(Clearance, ClearanceAdmin)
admin.site.register(Review, ReviewAdmin)