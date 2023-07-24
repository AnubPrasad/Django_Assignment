# from django.db import models

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)

# from django.db import models
# from django.contrib.auth.models import User

# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Work(models.Model):
#     WORK_TYPES = (
#         ('Youtube', 'Youtube'),
#         ('Instagram', 'Instagram'),
#         ('Other', 'Other'),
#     )

#     link = models.URLField()
#     work_type = models.CharField(max_length=20, choices=WORK_TYPES)
#     artists = models.ManyToManyField(Artist)

#     def __str__(self):
#         return f"Work ID: {self.id}, Type: {self.work_type}"

# accounts/models.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)


#                   artisit  object 
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     # Your existing fields for User model

#     # Add related_name for the reverse accessors to avoid clashes
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_set',  # Use a unique related_name for the groups field
#         blank=True,
#         help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
#         verbose_name='groups',
#     )

#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_set',  # Use a unique related_name for the user_permissions field
#         blank=True,
#         help_text='Specific permissions for this user.',
#         verbose_name='user permissions',
#     )

"""
code to add data in db

class Artist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Work(models.Model):
    LINK_TYPES = (
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=LINK_TYPES)
    artists = models.ManyToManyField(Artist, related_name='works')

    def __str__(self):
        return self.link
"""

# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    print("artist class da")
    print(name)
   # user_instance = models.ForeignKey(User, on_delete=models.CASCADE)
  #  work = models.ManyToManyField(Work)

    def __str__(self):
        print(self.name)
        return self.name


class Work(models.Model):
    YOUTUBE = 'YT'
    INSTAGRAM = 'IG'
    OTHER = 'OT'

    WORK_TYPES = [
        (YOUTUBE, 'Youtube'),
        (INSTAGRAM, 'Instagram'),
        (OTHER, 'Other'),
    ]

    link = models.URLField()
    work_type = models.CharField(max_length=2, choices=WORK_TYPES)
    artists = models.ManyToManyField(Artist, related_name='works')

    def __str__(self):
        return f"{self.get_work_type_display()} - {self.link}"

