from django.urls import path
from .views import about, home, teacher
from  django.contrib.auth import views as auth_views


urlpatterns = [
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('teacher/',teacher, name='teacher'),
    path('login/',auth_views.LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = "logout.html"), name='logout'),
]
