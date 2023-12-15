from django.db import models
from django.contrib.auth.models import User
import os
import uuid
from uuid import uuid4
from autoslug import AutoSlugField

def unique_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('media', filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ph_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True, 
        default='profile_pics/avatar.png'
    )
    
    create_at = models.DateField(null=True, blank=True, auto_now=True)
    update_at = models.DateField(null=True, blank=True, auto_now=True)
    delete_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username



class Courses(models.Model):  
 
    pic = models.ImageField(
        upload_to=unique_name,
        blank=True,
        null=True, 
        default='static/img/grid/grid_1.png'
    )    
    course_name  = models.CharField(max_length=150, blank=True)
    course_fee  = models.CharField(max_length=15, blank=True)
    course_description  = models.TextField(max_length=1000, blank=True,default=True)
    is_paid = models.BooleanField(default=True)   
    # slug = models.SlugField(unique=True, blank=True, null=True)
    slug = AutoSlugField(populate_from='course_name',unique=True, null=True,default='course_name')
     

    COURSE_STATUS_CHOICES = [
            ('active', 'Active'),
            ('inactive', 'Inactive'),
        ]
    course_status = models.CharField(max_length=10, choices=COURSE_STATUS_CHOICES, default='active')  
    
    created_at = models.DateField(auto_now_add=True)  
    
  
    def __str__(self):
        return self.course_name  
    
  
class lessons(models.Model):
    lesson_title = models.CharField(max_length=50)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    lesson_order = models.IntegerField()
  

    def __str__(self):
        return self.lesson_title

class Video(models.Model):
    video_title = models.CharField(max_length=50)
    lesson = models.ForeignKey(lessons, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=250, help_text='Thumbnail location name')
    video_upload_url = models.CharField(max_length=250, help_text='Video url')
    note = models.TextField(blank=True, null=True)
    video_file = models.CharField(max_length=250, help_text='Video location name')
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.video_title
    
class Reviews(models.Model):  
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"Review #{self.id} for {self.course.course_name} by {self.user.username}"    