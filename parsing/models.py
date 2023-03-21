from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name='марка авто')
    link = models.CharField(max_length=2083, verbose_name='ссылка')
    content = models.CharField(max_length=2083, verbose_name='описание')
    price = models.CharField(max_length=200, verbose_name='цена')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
