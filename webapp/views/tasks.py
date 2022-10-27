from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from webapp.forms import TaskForm
from webapp.models import Task


class TaskCreate(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskView(DetailView):
    template_name = 'task.html'
    model = Task


class TaskUpdateView(UpdateView):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')
