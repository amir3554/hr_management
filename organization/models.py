from django.db import models
from hr.models import Specialization, Employee


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=512)
    phone = models.CharField(max_length=64)
    email = models.EmailField("email", max_length=254, unique=True)
    logo = models.FileField(upload_to='company_logo/', null=True, blank=True)


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    manager = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)


