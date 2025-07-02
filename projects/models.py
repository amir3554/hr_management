from django.db import models
from organization.models import Company, Department
from hr.models import Employee


class Status(models.IntegerChoices):
    PENDING = 0, 'pending'
    COMPLETED = 1, 'completed'
    CANCELED = 2, 'canceled'

class TaskStatus(models.IntegerChoices):
    PENDING = 0, 'pending'
    COMPLETED = 1, 'completed'
    IN_PROGRESS = 2, 'in_progress'
    OVERDUE = 3, 'overdue'


class Priority(models.IntegerChoices):
    HIGH = 0, 'high'
    MEDIUM = 1, 'medium'
    LOW = 2, 'low'


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(choices=Status.choices, default=Status.PENDING)


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=TaskStatus.choices, default=Status.PENDING)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.MEDIUM)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)

