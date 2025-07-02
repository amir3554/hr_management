from django.db import models
from django.contrib.auth.models import AbstractUser
from organization.models import Company, Department


class Permession(models.IntegerChoices):
    OWNER = 0, 'owner'
    MANAGER = 1, 'manager'
    ADMIN = 2, 'admin'
    SUPER_USER = 3, 'super_user'
    HR_MANAGER = 4, 'hr_manager'
    DEPARTMENT_MANAGER = 5, 'department_manager'
    PROJECT_MANAGER = 6, 'project_manager'
    TASK_MANAGER = 7, 'task_manager'
    VIP = 8, 'vip'
    EMPLOYEE = 9, 'employee'
    OTHER = 10, 'other'


class Specialization(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Role(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    permession = models.IntegerField(choices=Permession.choices, default=Permession.EMPLOYEE)



class Employee(AbstractUser):
    email = models.EmailField('email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    employment_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=16, unique=True)
    picture = models.FileField(upload_to='employee_picture/',null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    bio = models.TextField(max_length=3600, null=True, blank=True)


    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self) -> str:
        return f"{self.email} - {self.phone} - {self.role} - {self.specialization}"

    class Meta:
        db_table = 'employee'

