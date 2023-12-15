from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('cart',views.cart ,name="cart"),
    path('checkout',views.checkout ,name="checkout"),
    path('course-details/<slug:slug>',views.coursed ,name="coursed"),
   
    path('lesson/<slug:slug>',views.lesson ,name="lesson"),
    path('student-dashboard',views.stddash ,name="sdash"),
    path('student-enrolled-courses',views.stdenroll ,name="senrolled"),
    path('student-profile',views.stdprofile ,name="sprofile"),
    path('student-settings',views.stdsetting ,name="ssetting"),
    path('login',views.loginUser ,name="login"),
    path('signup',views.signup ,name="signup"),    
    path('course',views.course ,name="course"),
   
      
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
