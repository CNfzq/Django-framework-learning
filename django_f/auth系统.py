'''
    我们昨天登录admin时创建的用户信息是存放在哪里了呢?

    auth系统的数据表:
        auth_user                       #用户表
        auth_user_groups                #中间表（用户表和用户组表）
        auth_group                      #用户组表
        auth_group_permission           #中间表（用户组表和权限表）
        auth_permission                 #权限表
        auth_user_user_permission       #中间表（用户表和权限表）
        auth从表的名称我们就能看出,
                auth_user,auth_group,auth_permission分别存放了用户,用户组,权限的信息表.
                auth_user_groups,auth_group_permission,auth_user_user_permission三张表就是多对多的关系表

        User:User是auth模块中维护用户信息的关系模式(继承了models.Model), 数据库中该表被命名为auth_user.
        Group:User对象中有一个名为groups的多对多字段， 多对多关系由auth_user_groups数据表维护。Group对象可以通过user_set反向查询用户组中的用户。
        Permission:Django的auth系统提供了模型级的权限控制， 即可以检查用户是否对某个数据表拥有增(add), 改(change), 删(delete)权限。

auth系统中User模型常用属性和方法:
        username:用户名
        email:邮箱
        groups:多对多的组
        user_permission:多对多的用户权限
        is_staff:是否是admin的管理员
        is_active:是否激活，判断该用户是否可用
        is_superuser:是否是超级用户
        last_login:上次登录的时间
        date_joined:注册时间
        is_authenticated:是否验证通过了
        is_anonymous:是否是匿名用户
        set_password(raw_password):设置密码，传原生密码进去
        check_password(raw_password):检查密码
        has_perm(perm):判断用户是否有某个权限
        has_perms(perm_list):判断用户是否有权限列表中的某个列表

auth认证系统功能:
        create_user 创建用户  模型类.objects.create_user(username=username,password=password)  把用户信息加进去
        authenticate 验证登录
        login 记住用户的登录状态
        logout 退出登录
        is_authenticated 判断用户是否登录
        login_required 判断用户是否登录的装饰器

'''