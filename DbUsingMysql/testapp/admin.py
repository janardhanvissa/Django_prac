from django.contrib import admin
from .models import employee
# Register your models here.
class employeeAdmin(admin.ModelAdmin):
	list_display = ['name', 'dob', 'sal', 'email', 'phone', 'addr']


admin.site.register(employee, employeeAdmin)
