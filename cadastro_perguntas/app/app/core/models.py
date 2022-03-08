from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.db import models

from app.core.manager import UserManager

import re


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True, help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), _('invalid'))])
    email = models.EmailField(('email address'), unique=True)
    nome = models.CharField(max_length=256)
    phone = models.CharField(max_length=11)
    is_whatsapp = models.BooleanField('É Whatsapp?', default=True)
    is_staff = models.BooleanField('Está ativo?', default=False)
    is_active = models.BooleanField('É da equipe?', default=True)
    created_at = models.DateTimeField('Data de Cadastro', auto_now_add=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUERID_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        db_table = 'auth_user'
        verbose_name = 'Usuário'
