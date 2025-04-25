from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Course
from .models import Teacher
from .models import Player
from .models import Team

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Player)
admin.site.register(Team)
