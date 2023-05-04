from django.contrib import admin

from .models import Student, FeesStructure, TuitionPayment, Card, Clearance

class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_name","gender","course","session","date_of_birth","address","religion","telephone_no","nationality","marital_status")

admin.site.register(Student, StudentAdmin)


class FeesStructureAdmin(admin.ModelAdmin):
    list_display = ("academic_year","year_of_study","semester","functional_fees","course")

admin.site.register(FeesStructure, FeesStructureAdmin)

class TuitionPaymentAdmin(admin.ModelAdmin):
    list_display = ("fees_structure","amount_paid","payment_date","student")

admin.site.register(TuitionPayment, TuitionPaymentAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("student","status")

admin.site.register(Card,CardAdmin)

class ClearanceAdmin(admin.ModelAdmin):
    list_display = ("card","year_of_study","semester","academic_year","is_test_cleared","is_exam_cleared","is_library_cleared")

admin.site.register(Clearance, ClearanceAdmin)
