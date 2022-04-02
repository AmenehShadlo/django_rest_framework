from django.urls import path
from .views import student_List,book_Update,book_List,student_Details,student_Save,student_Update,student_Delete,Registeration_View

urlpatterns = [
        path("student_list",student_List.as_view()),
        path("book_list",book_List.as_view()),
        path("book_update/<pk>",book_Update.as_view()),
        path("student_details/<pk>",student_Details),
        path("student_save",student_Save),
        path("student_update/<pk>",student_Update),
        path("student_delete/<pk>",student_Delete),
        path("Registeration_View",Registeration_View),
        
]