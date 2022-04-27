from tabnanny import verbose
from turtle import circle
from django.db import models
from django.utils. translation import ugettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.

class Circle(models.Model):
    name = models.CharField(_('Nome'), max_length=50)

    class Meta:
        ordering = ['id']
        verbose_name = _('Círculo')
        verbose_name_plural = _('Círculos')

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= _('Usuário'))
    comment = models.TextField(_('Comentário'))
    circle = models.ForeignKey(Circle, on_delete=models.CASCADE, verbose_name= _('Círculo'))
    created_at = models.DateTimeField(_('Criado'), auto_now_add=True)
    read = models.BooleanField(_('Lido?'), default=False)

    class Meta: 
        ordering = ['id']
        verbose_name = _('Comentário')
        verbose_name_plural = _('Comentários')

    def __str__(self) -> str:
        return self.user.username