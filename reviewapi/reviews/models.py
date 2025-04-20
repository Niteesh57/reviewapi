from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, mobile, password=None):
        if not email:
            raise ValueError('Users must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, mobile=mobile)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, mobile, password):
        user = self.create_user(email, first_name, last_name, mobile, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    objects = UserManager()

    def __str__(self):
        return self.email


class Review(models.Model):
    product = models.CharField(max_length=255)
    rating = models.IntegerField()
    review = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews_created', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, related_name='reviews_updated', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
