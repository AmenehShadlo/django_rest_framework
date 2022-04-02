from http.client import responses
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .models import Book, Student
from .serializers import StudentSerializer,UserSerializer,BookSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,UpdateAPIView
from .permissios import IsAuthor, IsSuperUserOrReadOnly


# @api_view(["GET"])
# @permission_classes((IsAdminUser,))
# def student_List(requset):
#     students=Student.objects.all()
#     students_serialize=StudentSerializer(students,many=True)
#     return Response(students_serialize.data)

class student_List(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    permission_classes=((IsSuperUserOrReadOnly,))

class book_List(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=((IsAuthenticated,))

class book_Update(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    permission_classes=((IsAuthor,))

@api_view(["GET"])
def student_Details(requset,pk):
    student=Student.objects.get(id=pk)
    student_serialize=StudentSerializer(student,many=False)
    return Response(student_serialize.data)

@api_view(["POST"])
def student_Save(request):
    student=StudentSerializer(data=request.data)

    if student.is_valid():
        student.save()
    
    return Response(student.data)

@api_view(["POST"])
def student_Update(request,pk):
    instance=Student.objects.get(id=pk)
    student=StudentSerializer(instance=instance, data=request.data)

    if student.is_valid():
        student.save()
    
    return Response(student.data)  

@api_view(["DELETE"])
def student_Delete(request,pk):
    instance=Student.objects.get(id=pk)
    instance.delete()

    return Response("Student Deleted!")

@api_view(["POST"])
def Registeration_View(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user=serializer.save()
            data["message"]="Register is done!"
            data['token']=Token.objects.get(user=user).key  
        return Response(data)  

