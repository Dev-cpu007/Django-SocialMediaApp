from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup/',views.signup,name = 'signup'),
    path('signin/',views.signin,name = 'signin'),
    path('settings/',views.settings,name = 'settings'),
    path('upload/',views.upload,name = 'upload'),
]
