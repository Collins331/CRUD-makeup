from django.db import models

# Create your models here.
# - class_name
# - number_of_students
# - logo_image
# - class_teacher
# - mentor

class School(models.Model):
    class_name = models.CharField(max_length=50)
    number_of_students = models.IntegerField()
    teacher = models.CharField(max_length=30)
    mentor = models.CharField(max_length=30)
    image = models.ImageField(upload_to='school/')


