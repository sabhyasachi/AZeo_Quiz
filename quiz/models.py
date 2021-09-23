from django.db import models

from student.models import Student
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Course(models.Model):
   course_name = models.CharField(max_length=50)
   question_number = models.PositiveIntegerField()
   total_marks = models.PositiveIntegerField()
   def __str__(self):
        return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=RichTextUploadingField()
    option1=RichTextUploadingField()
    option2=RichTextUploadingField()
    option3=RichTextUploadingField()
    option4=RichTextUploadingField()
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='')
    college=models.CharField(max_length=100,default='')
    mobile = models.CharField(max_length=20,null=False,default='')
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

