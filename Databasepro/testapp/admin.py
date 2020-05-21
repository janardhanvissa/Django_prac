from django.contrib import admin
from testapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):       #is to display list in the admin interface when we click  in the class.
	list_display = ['eno', 'ename', 'esal', 'eaddr']


admin.site.register(Employee, EmployeeAdmin)

