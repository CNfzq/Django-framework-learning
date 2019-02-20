from django.db import models

# Create your models here.

# 学院信息类（表）
class Department(models.Model):
    d_id=models.AutoField(primary_key=True)
    d_name=models.CharField(max_length=30)
    def __str__(self):
        return 'Department<d_id=%s,d_name=%s>'%(self.d_id,self.d_name)
'''
student.department  学生的所属学院
department.student_set  学院的学生
用related_name重命名反向查询关键字：department.student   学院的学生（调用related_name参数定义的命名）
默认的名字：类名(小写)__set   =   重命名的名字related_name=''
'''
# 学生基本信息表
class Student(models.Model):
    s_id=models.AutoField(primary_key=True)
    s_name=models.CharField(max_length=30)
    department=models.ForeignKey('Department',on_delete=models.CASCADE,related_name='student')    #on_delete是必须要的参数，指级联删，你删了我也跟着删。还可以设置其他的方式：你删了，我只显示null
    # 用related_name重命名反向查询(xxx__set)关键字,一般写在需要反向查询的外键那
    # department字段(表示的是学院id)设置的是外键，即要关联的表，通过映射在数据库显示的字段一般是xxx_id(即department_id)
    def __str__(self):
        return 'Student<s_id=%s,s_name=%s>'%(self.s_id,self.s_name)

# 学生课程信息表
class Course(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=30)    #课程名
    student=models.ManyToManyField('Student')  #没有什么级联删除的了，因为在数据库层面，会自动帮我们生成关系表（中间表也就是第三张表），无论你怎么删除，我都不会受影响，数据在第三张表里
    # course字段设置的是多对多的表关系，关联的表是Student,在数据库显示的表是course_student
    def __str__(self):
        return 'Course<c_id=%s,c_name=%s>'%(self.c_id,self.c_name)

# 学生详细信息表
class StudentDetail(models.Model):
    sd_id=models.AutoField(primary_key=True)     #一对一还会生成主键的
    sd_age=models.IntegerField()
    sd_gender=models.BooleanField()
    # sd_addr=models.CharField(max_length=30,null=True)
    s_sd= models.OneToOneField('Student',on_delete=models.CASCADE)   #外键+唯一
    # s_sd字段设置的是一对一关系，关联的表是Student,在数据库显示的是xxx_id(即s_sd_id)
    # 由于是一对一的表关系，在哪张表设置外键都是可以的
    def __str__(self):
        return 'StudentDetail<id=%s,age=%s,gender=%d,addr=%s,s_sd=%s>'%(self.sd_id,self.sd_age,self.sd_gender,self.sd_addr,self.s_sd)


