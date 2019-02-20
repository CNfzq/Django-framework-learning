from django.shortcuts import render

# Create your views here.
'''表建好了，开始对表的基本操作'''
from .models import *
from django.http import HttpResponse
# # 添加数据
# def add_data(request):
#     # 学院表的数据添加
#     # department=Department(d_name='文学院')
#     # department.save()
#     # 学生基本表的数据添加
#     # student=Student(s_name='辣椒',department_id=2)
#     # student.save()
#     # 学生详细表的数据添加
#     # studentdetail=StudentDetail(sd_age=21,sd_gender=0,sd_addr='浙江',s_sd_id=2)
#     # studentdetail.save()
#     # 课程表的数据添加
#     course=Course(c_name='C')
#     course.save()
#     return HttpResponse('添加成功')
#
# # 查询数据
# def search_data(request):
#     s1=Student.objects.get(s_id=1)     #学生的一个实例对象
#     print(s1.department)         #这里的department是Student表的字段，也是外键。返回的是类的实例(Department类的实例，也就是一条数据)
#     print(s1.department_id)       #所属学院的ID
#
#     d1 = Department.objects.get(d_id=1)  #学院的一个实例对象
#     print(d1)
#     print(d1.d_name)         #防问Department表里面的字段
#     # 查询学院里面有多少学生，通过反查管理器去查询（xxx_set方法），该反查管理器提供了很多查询方法
#     print(d1.student_set)       #返回的是None值（表关系.Student.None）所有的数据都在这个管理器里
#     print(d1.student_set.all())  #使用all()方法，拿到管理器里面所有的数据，返回的类型是QuerySet
#
#     # 学生想要更换学院
#     # 第一种方法：更改学生的学院属性
#     s2=Student.objects.get(s_name='辣椒')
#     s2.department_id=1
#     s2.save()
#     # 或者
#     s3=Student.objects.filter(s_name='方志强')
#     s3.update(department=2)
#     # 第二种方法：通过反查管理器(xxx_set)里面的方法add()，即可添加成功
#     d2=Department.objects.get(d_id=2)
#     d2.student_set.add(s2)        #把一个学生添加进学院，通过这种方式改变学生所属的学院
#
#     # add()方法，一对多，多对多添加数据（修改数据）
#     # create()方法，添加不存在的数据，新建
#     d2.student_set.create(s_name='李子')
#     d2.student_set.create(s_name='小付',department_id=1)
#
#     # remove()方法，在约束条件null=True的情况下使用，删除数据，多对多表关系下使用的多（第三张表删除，其他表未受影响）
#     return HttpResponse('查询成功')

'''表关联对象方法'''
# def test(request):
#     """
#     # 拿到数据
#     d1=Department.objects.get(d_id=1)     #学院表的第一条数据
#     s1=Student.objects.get(s_id=1)        #学生基本表的第一条数据
#     stu_detail=StudentDetail.objects.get(sd_id=1)  #学生详细表的第一条数据
#     c1=Course.objects.get(c_id=1)                  #课程表的第一条数据
#     '''关联表对象的访问'''
#     # 正向查就是：.属性
#     # 反向查就是：对象.类名小写_set
#     '''一对多'''
#     print(s1.department)         #学生的所属学院，正向查询（Student模型类的字段department），返回的是department表的一条数据
#     print (s1.department_id)
#     # 反向查询，学院所拥有的全部学生
#     print(d1.student_set.all())  #学院的所有学生
#
#     '''一对一'''
#     print(stu_detail.s_sd)
#     print(s1.s_id)
#     '''多对多'''
#     print(c1.student)    #报名这个课程的所有学生
#     print(s1.course_set.all())   #学生报名了哪些课程
#
#     '''反向管理器中的方法'''
#     # add()方法，数据的修改对象必须存在，参数必须是实例对象，而不是QuerySet,多个实例用逗号，隔开
#     # 一对多
#     wenxy=Department.objects.get(d_id=2)
#     wenxy.student_set.add(s1)
#     # 多对多
#     java=Course.objects.get(c_name='java')
#     python=Course.objects.get(c_name='python')
#     s1.course_set.add(java,python)
#     # create()方法，新建数据
#     # 一对多
#     wenxy.student_set.create(s_name='小屋')  #插班生
#     wenxy.student_set.create(s_name='小克')  #交换生
#     # 多对多
#     # python课程新加入了一个新学生，同时将信息传入两张表里面
#     python.student.create(s_name='狒狒',d_id=1)
#     s1.course_set.create('日语')
#     # remove()方法：删除数据
#     # 多对多
#     python.student.remove(d1)
#     # clear()方法：清空所有数据
# """
# ''' 多表查询,模型类(小写)+下划线（__）+字段名称'''
#     # 查询学院名字为‘软件学院’的学生的信息
#     result=Student.objects.filter(department__d_name='软件学院')
#     print(result)
#     # 查询学生名字中包含‘小’的学生的学院信息
#     result1=Department.objects.filter(student__s_name__contains='小')
#     print(result1)
#     # 查询学号为1的学生所有的课程
#     result2=Course.objects.filter(student__s_id=1)
#     print(result2)
#     # 报名java课程的所有学生
#     result3=Student.objects.filter(course__c_name='java')
#     print(result3)
#     # 报了‘python’课程的学生的所属学院的信息
#     result4=Department.objects.filter(student__course__c_name='python')
#     print(result4)
#     # 只要关联关系的，能过访问的就可以查询
#     return HttpResponse('哈哈哈')

'''模型补充内容'''
# 聚合查询:aggregate()是QuerySet 的一个终止子句（也是QuerySet的一个方法，叫聚合方法，方法里面可以使用各种函数）,它返回一个包含一些键值对的字典
# all()方法返回的是QuerySet对象，该对象提供了聚合方法可调用，即aggregate()
from django.db.models import Avg,Max,Min,Sum,Count,F,Q  #导入各种函数
from Database.models import User
def query_user(request):
    # rs=User.objects.all().aggregate(Avg('age'),Max('age'),Min('age'),Sum('age'))
    # print(rs)
    # #也可以指定一个名字
    # rs1 = User.objects.all().aggregate(average_age=Avg('age'))


    # 分组查询:为调用的QuerySet中每一个对象都生成一个独立的统计值（annotate()方法）
    from 表关系.models import Student,Course,StudentDetail
    # 以学院作为分组（学生的所属学院），查这个学院里面有多少个学生
    '''一对一的关系'''
    rs2=Student.objects.values('department')  #返回一个字典形式
    print(rs2)
    rs3=Student.objects.values('department').annotate(count=Count('department')).values('department_id','count')
    print(rs3)
    rs4=Student.objects.values('department').annotate(count=Count('department')).values('department__d_name','count')
    print(rs4)
    '''多对多的关系'''
    # 以某一门课程有多少学生
    c1=Course.objects.all()
    print(c1)
    # 课程的学生
    c2=Course.objects.all().annotate(count=Count('student')).values('c_name','count')
    print(c2)
    # 学生的课程数量
    c3=Student.objects.all().annotate(count=Count('course')).values('s_name','count')
    print(c3)

    # F查询: 针对两个字段的值的比较，F先拿到原来的值，在原来值的基础之上进行修改
    st=StudentDetail.objects.all().update(sd_age=F('sd_age')+1)   #先拿到原始的值age,原始age值+1，在赋给新的变量age，最后更新
    print(st)

    # Q查询:  如果你需要执行更复杂的查询（例如OR语句），你可以使用Q对象。(就是多条件查询呀)
    # Q对象可以使用&（and）、|（or）操作符组合起来
    # 使用~（not）操作符在Q对象前表示取反

    # 查询条件为name=fzq,age=21
    user=User.objects.filter(Q(name='fzq')&Q(age=21))
    print(user)
    user1 = User.objects.filter(Q(name='fzq') & ~Q(age=21))    #取反查询
    print(user1)
    return HttpResponse('哈哈哈哈')