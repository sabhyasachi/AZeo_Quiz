from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default='')
    #profile_pic= models.ImageField(upload_to='profile_pic/Student/',null=True,blank=True,default="")
    #address = models.CharField(max_length=40)
    email = models.EmailField(default='')
    college=models.CharField(max_length=100,default='')
    mobile = models.CharField(max_length=20,null=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
         return self.user.first_name