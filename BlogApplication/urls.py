from django.contrib import admin
from django.urls import path
from app.views import home , viewallpost , addlikepost , CustomerRegistrationView , logoutby , addcommnetinpost , getlikepost
from django.contrib.auth import views as auth_views  
from app.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('post/<int:id>/',viewallpost,name='post'),
    path('addlike/<int:id>/',addlikepost,name='addlike'),
    path('login/', auth_views.LoginView.as_view(template_name='./login.html', authentication_form=LoginForm), name='login'),
    path('registration/',CustomerRegistrationView.as_view(), name='customerregistration'),
    path('addcomment/<int:id>/',addcommnetinpost,name='addcomment'),
    path('logout/',logoutby,name='logout'),
    path('like/<int:id>/',getlikepost,name='like')
    
]
