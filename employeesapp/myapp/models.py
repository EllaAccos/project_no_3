from django.db import models

# Create your models here.

class employee(models.Model):
    FIRST_NAME = models.CharField(max_length=50)
    LAST_NAME = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50)
    PHONE_NUMBER = models.CharField(max_length=20)
    HIRE_DATE = models.DateField()
    JOB_ID = models.CharField(max_length=20)
    SALARY = models.IntegerField()
    COMISSION_PCT = models.IntegerField()
    MANAGER_ID = models.CharField(max_length=10)
    DEPARTMENT_ID = models.IntegerField()
    IMAGE = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.FIRST_NAME