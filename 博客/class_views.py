'''
补充内容：类视图
前面学习的内容都是以函数类型的视图,其实也可以使用类视图View，里面提供了基本的几个请求方式’：
        http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

        类视图（View）是以请求方式（get，post之类的）来分的，重写请求方法，然后匹配
        那自定义的函数可以用什么类的视图来包装呢？？？
        可以使用通用视图(generic)

'''
from .models import BlogModel
from django.shortcuts import render,redirect,reverse
from django.views import View    #导入类视图
class Blog_Add(View):            #继承类视图，可以使用里面所有的方法
    def get(self,request):                #重写父类里的方法
        return render(request,'demo_add.html')
    def post(self,request):
        print(request.POST)  #返回的是一个字典形式
        title = request.POST.get('title')
        content = request.POST.get('content')
        bm = BlogModel(title=title,content=content)
        bm.save()
        return redirect(reverse('class_add'))


from django.views.generic import TemplateView,ListView,DetailView #导入通用视图
class Blog_index(TemplateView):
    #模板的位置template_name
    template_name = 'demo_index.html'         #相当于return render(request,'demo_index.html')，使用类class定义视图很方便
class Blog_list(ListView):
    blog_list = BlogModel.objects.all()
    template_name = 'demo_list.html'
    #模板要用到的占位符(变量)，要传进去，相当于context={'blog_list':blog_list}
    context_object_name = 'blog_list'
    #模型类传进去
    model = BlogModel

class Blog_detail(DetailView):
    template_name = 'demo_detail.html'
    context_object_name = 'blog'
    model = BlogModel
    pk_url_kwarg='blog_id'