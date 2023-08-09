from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    school_id = models.CharField(max_length=10, blank=True, default='0')  # Default value as a string
    school_class = models.CharField(max_length=10, blank=True)
    telephone_number = models.CharField(max_length=15, blank=True)
    can_post = models.DecimalField(max_digits=1, decimal_places=0, default=1)
    is_teacher = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    is_verified = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    
    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(Group, related_name='users')
    user_permissions = models.ManyToManyField(Permission, related_name='users')

CustomUser = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    klasse = models.CharField(max_length=2)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    deadline = models.DateTimeField()
    ersteller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    teacher = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    verified = models.DecimalField(max_digits=1, decimal_places=0, default=0)

    def __str__(self):
        return self.title

    @property
    def teacher(self):
        return self.ersteller.is_teacher
    @property
    def verified(self):
        return self.ersteller.is_verified