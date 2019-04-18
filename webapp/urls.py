from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.student_profile, name='profile'),
    path('cv/', views.cv, name='cv'),
    path('jobs/', views.show_jobs, name='show_jobs'),
    path('jobs/add', views.add_job, name='add_jobs'),
    path('jobs/<int:ID>', views.view_job, name='view_job'),
    path('search/', views.search_skill, name='search_skill'),
]
