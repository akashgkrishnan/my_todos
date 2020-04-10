from home.models import todo_items
from django.forms import ModelForm


class TodoForm(ModelForm):
	class Meta:
		model = todo_items
		fields = ['task_name']