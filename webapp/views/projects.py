from django.urls import reverse
from django.views.generic import CreateView, DetailView
from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectCreate(CreateView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    model = Project

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class ProjectView(DetailView):
    template_name = 'project.html'
    model = Project
