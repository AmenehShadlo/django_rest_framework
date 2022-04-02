from django.urls import path
from .views import student_List,student_save

urlpatterns = [
      path("student_list",student_List),
      path("student_save",student_save)
]