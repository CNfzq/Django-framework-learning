'''
登录页面和注册页面都会用到form表单来提交数据
当数据提交到后台后,需要在视图函数中去验证数据的合法性.
django中提供了一个form表单的功能,这个表单可以用来验证数据的合法性还可以用来生成HTML代码
今天的登录注册案例我们就来使用这个django自带的form来生成前端页面以及验证数据.

关于django form表单的使用:
    1. 创建一个forms.py的文件,放在指定的app当中,然后在里面写表单.
    2. 表单是通过类实现的,继承自forms.Form,然后在里面定义要验证的字段.
    3. 在表单中,创建字段跟模型是一模一样的,但是没有null=True或者blank=True等这几种参数了,有的参数是required=True/False.
    4. 使用is_valid()方法可以验证用户提交的数据是否合法,而且HTML表单元素的name必须和django中的表单的name保持一致,否则匹配不到.
    5. is_bound属性:用来表示form是否绑定了数据,如果绑定了,则返回True,否则返回False.
    6. cleaned_data:这个是在is_valid()返回True的时候,保存用户提交上来的数据.
form表单中的一些参数说明:
    max_length  最大长度
    min_length  最小长度
    widget  负责渲染网页上HTML 表单的输入元素和提取提交的原始数据
    attrs  包含渲染后的Widget 将要设置的HTML 属性
    error_messages 报错信息
    注:虽然form可以生成前端页面,但这个功能实际用的少,主要是是用form表单的验证功能.
'''

from django import forms

# 这里的form可以直接生成前端的表单，也可以有验证的功能
class Login(forms.Form):        #继承模型类Form
    username=forms.CharField(min_length=4,max_length=10)   #设置范围，最小到最大
    password=forms.CharField(min_length=6,max_length=8,widget=forms.PasswordInput())   #widget:密文显示密码

# 注册模型类
class Register(forms.Form):
    username = forms.CharField(max_length=20,min_length=6)
    password = forms.CharField(max_length=8,min_length=6,widget=forms.PasswordInput(attrs={'placeholder':'请输入密码'}),
                               error_messages={'min_length': '密码长度小于6','max_length': '密码长度超过8了'})
    password_repeat=forms.CharField(widget=forms.PasswordInput())
    email=forms.EmailField()