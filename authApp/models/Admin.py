from django.db import models
from django.contrib.auth.models  import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class AdminManager (BaseUserManager):

    def create_user (self, username, password = None):

        if not username:
            raise ValueError('Ingrese un Usuario Válido')
        
        user = self.model(username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser (self, username, password):

        user = self.create_user (
            username = username,
            password = password,
        )

        user.is_admin = True
        user.save(using = self._db)
        return user
    
class Admin (AbstractBaseUser, PermissionsMixin):

    admin_id    = models.BigAutoField(primary_key = True)
    username    = models.CharField('Username', max_length = 50, unique = True)
    password    = models.CharField('Contraseña', max_length = 100)

    def save (self, **kwargs):

        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = AdminManager()
    USERNAME_FIELD = 'username'


