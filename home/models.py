from __future__ import unicode_literals
from django.db import models
from datetime import datetime

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, formData):
        errors = {}
        if len(formData['name']) < 5:
            errors["title"] = "Title should be at least 5 characters"
        if len(formData['content']) < 15:
            errors["content"] = "Network should be at least 15 characters"
        return errors

class Description(models.Model):
    content = models.TextField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description,related_name="course",on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)