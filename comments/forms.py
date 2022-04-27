from django.template.loader import render_to_string
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings

from .models import Comment

class SearchForm(forms.Form):
    query = forms.CharField(label=_('Localizar perfil'), max_length=100, required=True,
    widget=forms.TextInput(attrs={
        'placeholder': _('Campo Obrigatório. Informe nome, sobrenome ou usuário do perfil desejado.'),
        'autofocus': 'autofocus'
        })
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['circle', 'comment']
        

    def send_email(self, form, recipient_list, template_email):
        subject = 'Novo feedback'
        message = render_to_string(template_email)
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
     