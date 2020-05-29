from rest_framework import serializers
from .models import employee


class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['FIRST_NAME','LAST_NAME', 'EMAIL','PHONE_NUMBER', 'HIRE_DATE' ,'JOB_ID', 'SALARY','COMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID','IMAGE']



