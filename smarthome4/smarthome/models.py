from django.db import models

# Create your models here.
class Channel(models.Model):
    name = models.CharField('канал', max_length=256, primary_key=True)
    min = models.FloatField('Минимальное значение', null=True)
    max = models.FloatField('Максимальное значение', null=True)
    type =  models.BooleanField('управляющий', default=False)
#    value = models.CharField('значение', max_length=256)
#    data_type = models.CharField('тип данных', max_length=1, choices=[('d', 'числовые'), ('b', 'логические')])
    data = models.CharField('данные',max_length=100, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'канал'
        verbose_name_plural = 'каналы'









class Log(models.Model):
    kanal = models.CharField('Канал', max_length=256)
#    kanal = models.CharField('Канал', max_length=256, null=True)
    value = models.FloatField('значение', null=True)
    time = models.DateTimeField('Временная марка', auto_now_add=True)
#    data_type = models.CharField('тип данных', max_length=1, choices=[('d', 'ч$
#    data = models.CharField('данные',max_length=100, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Лог'
