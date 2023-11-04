from django.contrib import admin
from .models import Department,Patient_Record

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("Name","Diagnostics","Specialization")


class Patient_RecordAdmin(admin.ModelAdmin):
    list_display = ("Department_id","Created_date","Diagnostics")



admin.site.register(Department,DepartmentAdmin)
admin.site.register(Patient_Record,Patient_RecordAdmin)