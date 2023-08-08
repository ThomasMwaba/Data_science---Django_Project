from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=30)
    coding_test = models.IntegerField()
    writing_test = models.IntegerField()
    reading_test = models.IntegerField()
