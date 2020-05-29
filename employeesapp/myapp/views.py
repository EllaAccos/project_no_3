from rest_framework import viewsets, permissions
from .models import employee
from .forms import employeeserializer
from django.shortcuts import render,HttpResponse, redirect
# Create your views here.
class employeetview(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employeeserializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

def employee_id(request):
    employee1 = employee.objects.all()
    return render(request, 'HOME.html', {'employee1': employee1})

# def employee_view(request,):
#     employee2 = employee.objects.get(FIRST_NAME = FIRST_NAME)
#     return render(request, 'ID.html',{'employee2':employee2})