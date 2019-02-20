from django.urls import path
from . import views
urlpatterns=[
    path('log_reg_index/',views.log_reg_index,name='log_reg_index'),
    path('log_in/',views.login_i,name='log_in'),
    path('log_out/',views.logout_o,name='log_out'),
    path('reg/',views.register,name='reg'),

]