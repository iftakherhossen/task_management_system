from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=100)
    task_description = models.TextField()
    category = models.ManyToManyField(Category)
    is_completed = models.BooleanField(default=False)
    task_assigned_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.task_title