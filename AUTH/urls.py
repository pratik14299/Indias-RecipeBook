from django.urls import path
from . import views

urlpatterns = [
    path('reg/',views.userRegister,name='reg_url'),
    path('login/',views.loginUser,name='login_url'),
    path('logout/',views.logoutUser,name='logout_url')
]
