from django.urls import path
from .views import employee,Employeesview,Attandanceview,attanadnce,Userview,user

urlpatterns = [
    path("Employee/",Employeesview.as_view()),
    path("Employee/<int:id>/",employee),
    path("Employee/attandance/",Attandanceview.as_view()),
    path("Employee/attandance/<int:id>/",attanadnce),
    path("user/",Userview.as_view()),
    path("user/<int:id>/",user)



]