from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class ToDoModel(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=500,default='',null=True,blank=True)
    task_start_time = models.TimeField(default=datetime.now)
    task_end_time = models.TimeField(default=datetime.now()+timedelta(hours=1))
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

    class Meta:
        db_table = 'Todo'


