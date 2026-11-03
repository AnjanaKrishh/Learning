from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class CourseDb(models.Model):
    course_name = models.CharField(max_length=150)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    published_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name


class EnrollmentDb(models.Model):
    course = models.ForeignKey(
        CourseDb,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Enrolled')

    class Meta:
        unique_together = ('course', 'student')


