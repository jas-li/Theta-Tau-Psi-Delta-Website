from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Must have email address")

        if not password:
            raise ValueError("Users must have a password")

        if not first_name:
            raise ValueError("Users must have a first name")

        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name
        )

        user.active = is_active
        user.admin = is_admin
        user.staff = is_staff

        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_staffuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password=password, is_staff=True)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password=password, is_staff=True, is_admin=True)
        return user

class User(AbstractBaseUser):
    email 				= models.EmailField(verbose_name="email", max_length=255, unique=True)
    first_name          = models.CharField(max_length=255, blank=False, null=True)
    last_name           = models.CharField(max_length=255, blank=False, null=True)
    admin				= models.BooleanField(default=False)
    active				= models.BooleanField(default=True)
    staff				= models.BooleanField(default=False)
    timestamp           = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin