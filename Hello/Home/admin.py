from django.contrib import admin
from .models import Students,Results,Assignment,Teacher,Employee,Courses
# Register your models here.
admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(Courses)
admin.site.register(Assignment)
admin.site.register(Results)
admin.site.register(Employee)
