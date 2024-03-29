from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MySimpleModel(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=100)
    emp_name = models.CharField(max_length=100, blank=True, null=True)
    emp_post = models.CharField(max_length=100, blank=True, null=True)
    emp_salary = models.IntegerField(blank=True, null=True)

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username 