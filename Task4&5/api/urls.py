from django.urls import path
from . import views
urlpatterns = [
    path('createEmp/',views.createEmp),
    path('getEmp/',views.getEmp),
    path('createDep/',views.createDep),
    path('getDep/',views.getDep),
]
