from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse e-mail doit être fournie')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)  # Ce champ est requis pour l'authentification
    user_login = models.CharField(max_length=255)
    user_password = models.TextField()
    user_compte_id = models.IntegerField(unique=True)
    user_date_new = models.DateTimeField(auto_now_add=True)
    user_date_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_login']

    def save(self, *args, **kwargs):
        # Génère un compte_id si non défini
        if not self.user_compte_id:
            last_user = User.objects.all().order_by('user_compte_id').last()
            self.user_compte_id = last_user.user_compte_id + 1 if last_user else 1
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.user_login
