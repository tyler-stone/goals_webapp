from django.contrib import admin
from .models import Goal
from .models import SubGoal
from .models import Flag
from .models import Status
from .models import GoalType

# Register your models here.

admin.site.register(Goal)
admin.site.register(SubGoal)
admin.site.register(Flag)
admin.site.register(Status)
admin.site.register(GoalType)