from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
# Create your models here.


class GameUser(AbstractUser):
    static_wrong = models.IntegerField(
        verbose_name='Количество неверных ответов')
    static_correct = models.IntegerField(
        verbose_name='Количество верных ответов')

    def save(self, *args, **kwargs):
        if not self.id:
            self.static_correct = 0
            self.static_wrong = 0
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("profile_url", kwargs={"current_user_page_name": self.username})


class Mistake(models.Model):
    your_answer = models.CharField(
        verbose_name='Ошибочный ответ', max_length=50)
    correct_answer = models.CharField(
        verbose_name='Правильный ответ', max_length=50)
    user_didit = models.ManyToManyField(GameUser)
    count = models.IntegerField(verbose_name='Количество повторений ошибки', blank=True, null=True)
    def __str__(self):
        return self.your_answer


class EmphWord(models.Model):
    body = models.CharField(verbose_name='Слово',
                            max_length=150, db_index=True)

    def __str__(self):
        return self.body


class OvaWord(models.Model):
    body = models.CharField(max_length=150, db_index=True)
    correct = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.body + ' - ' + self.correct


class PreWord(models.Model):
    body = models.CharField(max_length=150, db_index=True)
    correct = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.body + ' - ' + self.correct


class ZnakWord(models.Model):
    body = models.CharField(max_length=150, db_index=True)
    correct = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.body + ' - ' + self.correct


class IiWord(models.Model):
    body = models.CharField(max_length=150, db_index=True)
    correct = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.body + ' - ' + self.correct
    
    
class ChikWord(models.Model):
    body = models.CharField(max_length=150, db_index=True)
    correct = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.body + ' - ' + self.correct
    
    
class OyoWord(models.Model):
    body = models.CharField(max_length=150, db_index=True)
    correct = models.CharField(max_length=10, db_index=True)

    def __str__(self):
        return self.body + ' - ' + self.correct