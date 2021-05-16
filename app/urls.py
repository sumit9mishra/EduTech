from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.homeView.as_view(),name='home'),
    path('login/',views.login,name='login'),
    path('registration/', views.StudentRegistrationView.as_view(),name = 'registration')
    
]
