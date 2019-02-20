from django.urls import path
from . import views
urlpatterns=[
    path('user_index',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

]