from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )

    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    admission_date = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.student_id} - {self.name}"