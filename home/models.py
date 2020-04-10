from django.db import models

# Create your models here.

class todo_items(models.Model):
	task_name = models.CharField(max_length=40)
	task_status = models.BooleanField(default=False)

	def __str__(self):
		return self.task_name
