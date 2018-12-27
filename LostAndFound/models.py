from django.db import models


class Item(models.Model):
    item_type=(
        ('证件','证件类'),
        ('电子','电子类'),
        ('书本','书本类'),
        ('其他','其他类')
    )
    name = models.CharField(default='请输入名称', max_length=30, verbose_name='物品名称')
    address = models.CharField(default='请输入地点', max_length=30, verbose_name='丢失地点')
    type = models.CharField(default='证件类',max_length=30 ,choices=item_type, verbose_name='物品类型')
    phone = models.CharField(default='0000000000', max_length=11, verbose_name='手机号')
    image = models.ImageField(default='',verbose_name='图片')
    add_time = models.DateField(default='',verbose_name='发布时间')
    isReturn = models.IntegerField(default='0',verbose_name='是否归还')

    class Meta:
        verbose_name = '物品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
