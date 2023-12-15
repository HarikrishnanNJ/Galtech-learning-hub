from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from . models import *


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,"index.html")

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")

def coursed(request,slug):
    detail = get_object_or_404(Courses, slug=slug)
    current_user = request.user
    
    if request.method == 'POST' and 'sub' in request.POST:
       
       
        rating = request.POST.get("rating")  
        review_text = request.POST.get("review_text")  
        Reviews.objects.create(user=current_user,course=detail, rating= rating,  review_text=review_text)
                         
    # for review in detail.reviews_set.all():
    #         print(review.course)
            
    # for lesson in detail.lessons_set.all():
    #     print(lesson.lesson_title)
    #     for video in lesson.video_set.all():  # Use the related_name 'videos'
    #         print(video.video_title)
               
    return render(request,"course-details.html",{'detail':detail})
def course(request):     
    course = Courses.objects.all()
    return render(request,'course.html', {'course':course})
   


def lesson(request,slug):
  
    course = Courses.objects.get(slug=slug)
    for lesson in course.lessons_set.all():
        print(lesson.lesson_title)

        for video in lesson.video_set.all():  # Use the related_name 'videos'
            print(video.video_title)
    return render(request,'lesson.html',{'course':course})

  


def stddash(request):
    return render(request,"dashboard/student-dashboard.html")

def stdenroll(request):
    return render(request,"dashboard/student-enrolled-courses.html")


def stdprofile(request):
    profile= UserProfile.objects.get(user=request.user)
    return render(request,'dashboard/student-profile.html',{'profile': profile})
    
   

def stdsetting(request):
    return render(request,"dashboard/student-settings.html")



def signup(request):
    if request.method == "POST":
      
         # Create user fields
        if 'register' in request.POST: 
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("email")
            password = request.POST.get("password")
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            
            # user liking user in Create profile
            user = user
            ph_number = request.POST.get("ph_number")
            profile_picture = request.FILES.get("profile_picture")
            # Create profile
            user_profile = UserProfile.objects.create(user=user, ph_number=ph_number, profile_picture=profile_picture)
            print(user_profile)
            # return render(request,"login.html")
    return render(request,"login.html")

def loginUser(request):
    if request.method == "POST":
        if 'login' in request.POST: 
            username = request.POST.get("username")
            password = request.POST.get("password")           
            print(  username,  password)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                # Redirect to a success page or do further processing
                return render(request,"index.html")   
            else:           
                return HttpResponse("Invalid login credentials. Please try again.")
       
        return render(request,"login.html")   
    else:
        return render(request,"login.html")         

  

