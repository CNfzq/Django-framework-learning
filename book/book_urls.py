'''URL配置文件（子路由）'''
from django.urls import path
from . import book_views
urlpatterns = [
    path('book_index/',book_views.book_index,{'fzq':'456'}),
    path('book_test/',book_views.book_test),
    path('article/<name>',book_views.article),
    path('article_newaaaaa/<name>',book_views.article_new,name='new_article'),
    path('temp/',book_views.get_temp),
    path('index/',book_views.index)
]