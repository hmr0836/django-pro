from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    title = models.CharField(max_length=255,unique=True)

    def __str__(self):  #建立表單
        return self.title

class Todo(models.Model):
    title = models.CharField('標題',max_length=255)
    content = models.TextField('內容',max_length=500)
    status = models.BooleanField('完成',default=False)
    tag = models.ManyToManyField(Tag,verbose_name='標籤') #Tag的建立要先寫在上面
    creator = models.ForeignKey(User,on_delete=models.PROTECT,verbose_name='建立')

    def __str__(self):
        return self.title

# Create your models here.
