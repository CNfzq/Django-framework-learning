from django.urls import path
from . import bk_views,class_views     #导入函数视图和类视图
urlpatterns=[
    # 函数视图
    path('index/',bk_views.index,name='blog_index'),
    path('add/',bk_views.add,name='blog_add'),
    path('list/',bk_views.list,name='blog_list'),
    path('detail/<blog_id>/',bk_views.detail,name='blog_detail'),
    path('edit/<blog_id>',bk_views.edit,name='blog_edit'),
    path('delete/<blog_id>',bk_views.delete,name='blog_delete'),
    # 类视图
    path('class_add/', class_views.Blog_Add.as_view(), name='class_add'),  #引用类，要调用类里面的方法就必须使用as_view(),会去调用类里面相应的方法
    #通用视图
    path('class_index/',class_views.Blog_index.as_view(),name='class_index'),
    path('class_list/',class_views.Blog_list.as_view(),name='class_list'),
    path('class_detail/<blog_id>/',class_views.Blog_detail.as_view(),name='class_detail'),
]


