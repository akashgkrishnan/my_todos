from django.shortcuts import render, redirect
from home.models import todo_items
from home.forms import TodoForm
# Create your views here.


def index(request):
	form = TodoForm()
	todos = todo_items.objects.order_by('-id')
	context = {'todos': todos, 'form': form}
	if request.method == 'POST':
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			print('hi')
			return redirect('index')

	return render(request, 'home/index.html', context)


def complete(request, todo_id):
	todo = todo_items.objects.get(pk = todo_id)
	todo.task_status = True
	todo.save()
	return redirect('index')
