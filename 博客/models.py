from django.db import models

# Create your models here.
#
class BlogModel(models.Model):
    title=models.CharField(max_length=100,blank=True)  # blank=:from表单的提交允许为空
    content=models.TextField()
