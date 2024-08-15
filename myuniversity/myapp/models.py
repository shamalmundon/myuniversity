from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    department_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to="media")
    def __str__(self):
        return self.department_name



class Courses(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    course_name=models.CharField(max_length=100)
    available_seats=models.PositiveIntegerField()
   
   
    def __str__(self):
        return self.course_name

class Exmreg(models.Model):
    Student_name=models.OneToOneField(User,on_delete=models.CASCADE)
    Address=models.CharField(max_length=250)
    # options=
    Nameofthe_department=models.ForeignKey(Department,on_delete=models.CASCADE)
    Nameofthe_course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    enrollment=models.PositiveIntegerField()

    def __str__(self):
        return self.Student_name


