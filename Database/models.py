'''
django自带的ORM：
1.ORM概念:对象关系映射（Object Relational Mapping,简称ORM）
2.ORM的优势:不用直接编写SQL代码，只需像操作对象一样从数据库操作数据。

        1. 模型类必须都写在app下的models.py文件中。
        2. 模型如果需要映射到数据库,所在的app必须被安装.
        3. 一个数据表对应一个模型类,表中的字段,对应模型中的类属性.

关于数据库的连接和映射：
            1.先安装MySql:pip install mysql
            2.再安装MySql的驱动器pymysql:pip install pymysql
            3.设置连接器为pymysql(必须要设置的):
                    在主目录下的的__init__.py文件添加下面两句
                    import pymysql
                    pymysql.install_as_MySQLdb()
            4.数据库的基本信息配置:
                    在主配置文件setting,py里面配置基本的数据库信息
            5.在app下面的models.py中创建django的模型类.
            6.1.首先执行以下命令,要创建映射文件：
                python  manage.py   makemigrations  [app_name]:命令后面可以跟app名称,表示指定对某个app的模型进行映射,没写所有的app都执行.
                2.执行以下命令,将映射文件中的映射数据提交到数据库中
                python  manage.py   migrate    :在执行前,保证我们创建模型的APP是已经注册过的APP
            7.将模型类映射到数据库:
                打开数据我们能看到创建的以app名_模型名的数据表,而其他的一些表格是django自动生成的.
                注意:如果要删除表,那么可以去django模型中注释掉模型类,然后执行映射的命令,不要手动在命令行里面去删除.
'''

from django.db import models
"""
常用的字段类型:
    1. IntegerField : 整型，映射到数据库中的int类型。
    2. CharField:  字符类型，映射到数据库中的varchar类型，通过max_length指定最大长度。
    3. TextField:  文本类型，映射到数据库中的longtext类型。
    4. BooleanField: 布尔类型，映射到数据库中的tinyint类型，在使用的时候，传递True/False进去。如果要可以为空，则用NullBooleanField。
    5. DateField:  日期类型，没有时间。映射到数据库中是date类型，
        在使用的时候，可以设置DateField.auto_now每次保存对象时，自动设置该字段为当前时间。设置DateField.auto_now_add当对象第一次被创建时自动设置当前时间。
        插入数据的时间
        数据修改更新的时间
    6. DateTimeField:   日期时间类型。映射到数据库中的是datetime类型，
        在使用的时候，传递datetime.datetime()进去。

Field的常用参数:
    primary_key:  指定是否为主键。
    unique:  指定是否唯一。
    null:  指定是否为空，默认为False。
    blank: 等于True时form表单验证时可以为空，默认为False。
    default:  设置默认值。
    DateField.auto_now:  每次修改都会将当前时间更新进去，只有调用，QuerySet.update方法将不会调用。这个参数只是Date和DateTime以及TimModel.save()方法才会调用e类才有的。（数据修改更新的时间）
    DateField.auto_now_add:  第一次添加进去，都会将当前时间设置进去。以后修改，不会修改这个值（插入数据的时间）


"""
# Create your models here.
# 创建类映射类（表）
class User(models.Model):
    id=models.AutoField(primary_key=True)  #可以省略的，django会自动帮我创建ID的
    name=models.CharField(max_length=30)
    age=models.IntegerField()

    # 假如需要添加新的字段，就必须加参数null=True或者加一个默认值default=''
    note=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=60,default='北京')

    #定义一个输出的函数，用于格式化我们需要的输出方式
    def __str__(self):
        return 'User<id=%s,name=%s,age=%d>'%(self.id,self.name,self.age)

# class Test(models.Model):
#     name=models.CharField(max_length=30)
#     age=models.IntegerField()

class Ftest(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    note=models.TextField(null=True)
    gender=models.BooleanField(default=True)          #设置默认值，一般1表示男  0是女
    create_time=models.DateField(auto_now_add=True)   #自动添加 插入数据的时间，第一次的时间，更新不修改
    updata_time=models.DateTimeField(auto_now=True)   #自动添加 数据修改更新的时间，实时修改
    def __str__(self):
        return 'Ftest<name=%s,age=%d,note=%s>'%(self.name,self.age,self.note)











