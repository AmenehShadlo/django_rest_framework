from django.http import response
from django.shortcuts import redirect, render
import requests
import json
# Create your views here.

def student_List(request):
    response=requests.get("http://127.0.0.1:8000/api_app/student_list").json()
    context={
        "students":response
    }

    return render(request,"testapp/studentlist.html",context)


def student_save(request):
    instance={"Name":"Reza","Family":"Akbari","Code":"65465465"}
    jsondata=json.dumps(instance)
    headers={'content-type':"application/json"}
    requests.post("http://127.0.0.1:8000/api_app/student_save",data=jsondata,headers=headers)

    return redirect(student_List)

def Save(request):
    if request.method=='POST':
        return render(request, "testapp/studentlist.html",{})
    else:
        return render(request, "testapp/save.html",{})

