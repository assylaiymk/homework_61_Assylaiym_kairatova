from django.urls import path

from webapp.views.projects import ProjectCreate, ProjectView
from webapp.views.tasks import TaskView, TaskUpdateView, TaskCreate, TaskDeleteView
from webapp.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('tasks/add/', TaskCreate.as_view(), name='task_add'),
    path('tasks/add/project', ProjectCreate.as_view(), name='project_add'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/confirm-delete/', TaskDeleteView.as_view(), name='confirm_delete'),
    path('tasks/', IndexView.as_view()),
    path('tasks/<int:pk>', TaskView.as_view(), name='task_detail'),
    path('tasks/project/<int:pk>', ProjectView.as_view(), name='project_detail')
]
