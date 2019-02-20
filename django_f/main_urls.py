"""配置URL的文件(主URL配置文件)，所谓的URL就是客户端输入要访问的地址"""

"""django_f URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include           #导入re_path,include
from . import main_views
# from book import book_views         #不用再主目录里面导入啦，可以在自己的app里面导入啦
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', main_views.hello),


    path('hello_taka/<name>/<int:age>',main_views.hello_taka),


    path('hello_fzq/',main_views.hello_fzq),
    # re_path 跟django1.11版本里面的url('',views) 是一样的
    re_path('hello_fzq11/',main_views.re_path_test),

    path('book/',include('book.book_urls'),{'fzq':'123'}),  #include()关联到子app里的urls文件里面的配置
    # path('book_index/', book_views.book_index)   #子app里面配置的url,现在不需要在主目录url文件里配置，在自己的子app里urls文件里配置，导入include

    path('workhome/',include('workhome.work_urls')),  #自己写作业的主路径

    path('',include('第3章.urls_3')),           #第3章的主路由路径
    path('',include('第4章.urls_4')),           #第4章的主路由路径
    path('',include('Database.urls_5')),
    path('',include('表关系.urls_6')),
    path('',include('博客.bk_urls')),
    path('',include('request_response.urls')),
    path('',include('cookie_session.urls')),
    path('',include('login_register.urls')),


]

