from email.policy import default
from symtable import Class
from tabnanny import verbose

from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return f'{self.title}, {self.text}, {self.published_at}, {self.image}'

class Tag(models.Model):
    tag_name = models.CharField(max_length=256)

class Scope(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной раздел', default=False)

