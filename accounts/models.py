from tabnanny import verbose
from tkinter.tix import Tree
from xml.sax.handler import DTDHandler
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class ProfileManger(models.Manager):

    def search(self, query):
        qs = self.get_queryset()
        if query:
            or_lookup = (models.Q(user__first_name=query )| models.Q(user__last_name=query) | models.Q(user__username__icontains=query) )
            qs = qs.filter(or_lookup)
        return qs


class Profile(models.Model):
    CHOICES_GENRE = (
        ('M', _('Masculino')),
        ('F', _('Feminino'))
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Usuário'))
    photo = models.ImageField(_('Foto'), upload_to='photos')
    bio = models.TextField(_('Mini bio'), blank=True)
    birthday = models.DateField(_('Nascimento'), blank=True)
    genre = models.CharField(_('Sexo'), max_length=1, choices=CHOICES_GENRE, blank=True)
    cell_phone = models.CharField(_('Celular'), max_length=14, blank=True)

    objects = ProfileManger()

    class Meta:
        ordering = ['id']
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfis')

    def __str__(self) -> str:
        return self.user.username

    
    @property
    def get_full_name(self):
        return self.user.get_full_name

    @property
    def get_username(self):
        return self.user.username