from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def showstudent(request):
    stu=student.objects.all()
    
    context={
       'stu':stu
   }
    return render(request ,"showstudent.html",context)

def removestudent(request,student_id=0):
    if student_id:
        try:
           s=student.objects.get(id=student_id)
           s.delete()
           return HttpResponse("deleted")
        except:
            return HttpResponse("please enter valid id")
    stu=student.objects.all()
    if(stu):
         context={
       'stu':stu
        }
    else:
        none="none"
        context={
       'stu':none
           
        }
    
        
   
       
    return render(request,"removestudent.html",context)

def addstudent(request):
    if request.method=="POST":
        name=request.POST.get("name")
        
        
        fathername=request.POST.get("fathername")
        mothername=request.POST.get("mothername")
        clas=request.POST.get("class")
        rollnumber=request.POST.get("rollnumber")
        email=request.POST.get("email")
        print(name)
        print(fathername)
        print(clas)
        detail=student(name=name,father_name=fathername,mother_name=mothername,clas=clas,role_number=rollnumber,email=email)
        detail.save()
    return render(request,"addstudent.html")


def findstudent(request):
    if request.method=='POST':
        name=request.POST.get('name')
         
        studen=student.objects.all()
        if name:
            stu=studen.filter(Q(name__icontains=name))
        
        context={
            'stu':stu
        }
   
        return render(request,"showstudent.html" ,context)
    return render(request,"findstudent.html" )
   