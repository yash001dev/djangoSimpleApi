from django.db import models
from django.contrib.auth.models import AbstractBaseUser,UserManager as AbstractUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Manager For Profile User
class UserProfileManager(AbstractUserManager):
    def create_user(self,email,name,password=None):
        # Create a new User Profile
        if not email:
            raise ValueError('User Must have an Email Address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        # Create and Save a New superUser with Given Details
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    # Databse model for users in the system
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        # Retrieve Full Name of User
        return self.name

    def get_short_name(self):
        #Retrieve Short Name of User
        return self.name
    
    def __str__(self):
        # Return String Representation Of Our User
        return self.email


