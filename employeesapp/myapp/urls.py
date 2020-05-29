from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'my_app_1'
router = routers.DefaultRouter()
router.register('employee',views.employeetview)
urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.employee_id, name = "HOME"),
    path('ID/', views.employee_id, name = "ID_PAGE")
]