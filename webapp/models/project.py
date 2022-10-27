from django.db import models


class Project(models.Model):
    title = models.CharField(verbose_name='Title', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Description', max_length=300, null=False, blank=False)
    start_date = models.DateTimeField(verbose_name='Date started', auto_now_add=True)
    end_date = models.DateTimeField(verbose_name='Date ended', auto_now=True)
    task = models.ForeignKey(to='webapp.Task', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.description}'
