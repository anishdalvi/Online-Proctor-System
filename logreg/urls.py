from django.urls import include, path
#from django.views.generic.base import TemplateView
from.import views

urlpatterns = [
    #path('',TemplateView.as_view(template_name='login.html'),name='usersite/'),
    path('', views.login, name='login'),
    #path('admission',views.login ),
    #path('usersite',views.login ),
    #path('usersite/',include('usersite.urls')),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('logout', views.logout_view, name='logout'),

    
]
