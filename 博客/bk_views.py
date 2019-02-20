from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import BlogModel
# Create your views here.
#主页
def index(request):
    return render(request,'demo_index.html')
#添加页
def add(request):
    if request.method=='GET':
        return render(request,'demo_add.html')
    elif request.method=='POST':
       print(request.POST)      #返回的是一个字典形式
       title=request.POST.get('title')
       content=request.POST.get('content')
       bm=BlogModel(title=title,content=content)
       bm.save()
       return redirect(reverse('blog_add'))

#列表页
def list(request):
    blog_list=BlogModel.objects.all()
    return render(request,'demo_list.html',context={'blog_list':blog_list})

#详情页
def detail(request,blog_id):
    blog=BlogModel.objects.get(id=blog_id)
    return render(request,'demo_detail.html',context={'blog':blog})

# 编辑文章操作
def edit(request,blog_id):
    blog = BlogModel.objects.get(id=blog_id)
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog.title=title
        blog.content=content
        blog.save()
        return redirect(reverse('blog_list'))
    return render(request, 'demo_edit.html', context={'blog': blog})





# 删除文章操作
def delete(request,blog_id):
    blog=BlogModel.objects.get(id=blog_id)
    if blog:
        blog.delete()
        return  redirect(reverse('blog_list'))
    else:
        return HttpResponse('此博客不存在')

