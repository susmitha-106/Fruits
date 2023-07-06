from django.urls import path
from. import views
from .views import change_password

urlpatterns = [
    path('', views.home,name="home"),
    path('fruits/', views.fruits, name='fruits'),
    path('fruits_list', views.fruits_list, name='fruits_list'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_user, name='login'),
    path('logout', views.handlelogout, name='logout'),
    path('profile',views.profile,name="profile"),
    path('change_password/', change_password, name='change_password'),
    path('Course_list/',views.course_list, name='course_list'),
    path('open_youtube_link/<int:course_id>/', views.open_youtube_link, name='open_youtube_link'),
    
    
    
    
]
