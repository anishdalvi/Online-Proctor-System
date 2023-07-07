from django.urls import path
from.import views
from django.contrib.auth import views as auth_views
#from usersite.views import submit_personalinfo

urlpatterns = [
    #path('', views.admission, name='admission'),
    path('admission', views.admission, name='admission'),
    path('submit_admission/', views.submit_admission, name='submit_admission'),
    path('academic', views.academic, name='academic'),

    path('achievementdetails', views.achievementdetails, name='achievementdetails'),
    path('personalinfo', views.personalinfo, name='personalinfo'),
    path('unauth', views.unauthorised, name='unauth'),
    path('logout', views.logout_view, name='logout'),
    path('logreg/login/', auth_views.LoginView.as_view()),
    path('submit_personalinfo/', views.submit_personalinfo, name='submit_personalinfo'),
    path('submit_academic/', views.submit_academic, name='submit_academic'),
     #path('submit_achievements/', views.submit_achievements, name='submit_achievements'),

]
