from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homeView.as_view(),name='home'),
    path('login/',views.login,name='login'),
    path('registration/', views.StudentRegistrationView.as_view(),name = 'registration'),
    path('changepassword/',views.change_password,name='changepassword'),
    path('webdevlopment/', views.webdevlopment,name ='webdevlopment'),
    path('learncloud/', views.learncloud, name='learncloud'),
    path('html/',views.HTML,name='html'),
    path('css/', views.CSS, name='css'),
    path('bootstrap/',views.Bootstrap,name='bootstrap'),
    path('javascript/', views.Javascript, name='javascript'),
    path('reactjs/',views.Reactjs,name='reactjs')




    
]
