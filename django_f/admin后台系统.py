'''
在项目的主目录（django_f）下有一个主路由的文件（urls.py）我们会看到这样一个url的配置：
    urlpatterns = [path('admin/', admin.site.urls)]
    这条路由就是进入admin后台系统的路径，可以访问一下
    发起请求后出现一个登录界面，让你输入用户名和密码去登录（那么怎么获取用户名和密码？？）
介绍 Django 管理页面:
    为你的员工或客户生成一个用户添加，修改和删除内容的后台是一项缺乏创造性和乏味的工作。因此，Django 全自动地根据模型创建后台界面。
    Django 产生于一个公众页面和内容发布者页面完全分离的新闻类站点的开发过程中。站点管理人员使用管理系统来添加新闻、事件和体育时讯等，这些添加的内容被显示在公众页面上。
    Django 通过为站点管理人员创建统一的内容编辑界面解决了这个问题。
    管理界面不是为了网站的访问者，而是为管理者准备的。
admin创建用户:
    运行命令,创建一个管理员账号:
    python manage.py createsuperuser
    按提示输入用户名、邮箱、密码
    然后用创建的用户登录
管理界面中国化:
    编辑settings.py文件，设置编码、时区
    LANGUAGE_CODE = 'zh-Hans'  #汉语
    TIME_ZONE = 'Asia/Shanghai'  #时区
向admin中注册模型:
    将之前在表关系中那几个模型类创建在现在的app的models.py中.
    将模型类执行映射在数据库中生成表.
    在app里面有个admin.py的文件,在这个文件中注册模型:
        admin.site.register()
admin后台页面显示:
    将模型类再admin.py中注册过后
    刷新管理页面,对数据表中数据进行增删改查操作


如果数据表不雅观，可根据自己的要求更改
自定义管理页面:
    Django提供了admin.ModelAdmin类
    通过定义ModelAdmin的子类，来定义模型在Admin界面的显示方式：
            列表页属性：
                list_display：显示字段，可以点击列头进行排序
                list_filter：过滤字段，过滤框会出现在右侧
                search_fields：搜索字段，搜索框会出现在上侧
                list_per_page：分页，分页框会出现在下侧
            添加、修改页属性：
                fields：属性的先后顺序
                fieldsets：属性分组
                注意：上面两个属性，二者选一。
自定义管理页面例子:
        创建模型类对应的管理页面admin的类
        将自定义的类放到register方法中注册使用

'''