from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Course
from .models import Teacher
from .models import Player
from .models import Team
from .models import Caddie
from .models import Member
from .models import Timeslot
from .models import MemberTeeTime

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Caddie)
admin.site.register(Member)
admin.site.register(Timeslot)
admin.site.register(MemberTeeTime)
