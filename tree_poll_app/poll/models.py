from django.db import models
from django.contrib.postgres.fields import ArrayField

from mptt.models import MPTTModel, TreeForeignKey


class Test(models.Model):
    title = models.CharField(max_length = 200, verbose_name='Название')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(MPTTModel):
    test = models.ForeignKey(Test, related_name='questions', on_delete = models.CASCADE)
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительский вопрос')
    choice_trigger = ArrayField(models.CharField(
        max_length=20, verbose_name='Номер триггер вопроса', null=True, blank=True
        ), null=True, blank=True)
    display = models.BooleanField(verbose_name='Видимость вопроса', default=True) 
 
    def __str__(self):
        return self.question_text
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200, verbose_name='Текст ответа')
    number_choice = models.CharField(max_length = 20, verbose_name='Номер ответа по порядку')
    votes = models.IntegerField(default = 0, verbose_name='Количество ответов')
 
    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'