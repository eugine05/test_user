from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
 
 
class UserAccountManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, telefon, password, **extra_fields):
        if not telefon:
            raise ValueError('telefon must be provided') 
        
        user = self.model(telefon=telefon, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, telefon=None, password=None, **extra_fields):
        return self._create_user(telefon, password, **extra_fields)
 
    def create_superuser(self, telefon, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
 
        return self._create_user(telefon, password, **extra_fields)
 
 
class User(AbstractBaseUser, PermissionsMixin):
 
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'telefon'
 
    objects = UserAccountManager()
 
    telefon = models.CharField('telefon', unique=True, blank=False, null=False, max_length=15)
    first_name = models.CharField('Имя', blank=True, null=True, max_length=20)
    patronymic = models.CharField('Отчество', blank=True, null=True, max_length=20)
    full_name = models.CharField('Фамилия', blank=True, null=True, max_length=20)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
 
    def get_short_name(self):
        return self.telefon
 
    def get_full_name(self):
        return self.telefon
 
    def __unicode__(self):
        return self.telefon
