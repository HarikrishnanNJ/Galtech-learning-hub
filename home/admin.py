from django.contrib import admin
from .models import Courses
from .models import UserProfile
from .models import lessons,Video,Reviews

class Video_TabularInline(admin.TabularInline):
    model=Video

class lessons_admin(admin.ModelAdmin):
    inlines=[Video_TabularInline]  
      
admin.site.register(UserProfile)
admin.site.register(Courses)
admin.site.register(lessons, lessons_admin)
admin.site.register(Video)
admin.site.register(Reviews)
