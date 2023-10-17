from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

#Types of users
# Create your models here.
# AbstactUser
# AbstractBaseUser

# Database relationships
# OneToOneField- 
# ForeignKey 

# class User(AbstractUser):
#     pass

# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

# customizing the user model
#AbstractBaseUser-
#BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name,last_name, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        
        if not username:
            raise ValueError("User must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name,last_name, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_superadmin = True
        user.is_active = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    HOSPITAL = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
        (HOSPITAL, 'hospital'),
        (CUSTOMER, 'customer')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
# class Profle -> User TOD0 -> Nimrod
    
    

