from django.urls import path
from . import views_4
urlpatterns = [
    path('04_index_01/<haha>',views_4.template_tag),
    path('04_index_02/<haha>',views_4.index_04,name='04_index_02'),  #url传参：接收其他路由里面的参数
    path('04_index_03/',views_4.index_05),           #模板继承与引用
    path('04_index_04/',views_4.index_06),
    path('04_index_05/',views_4.index_07)
]