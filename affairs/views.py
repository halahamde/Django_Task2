from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import myuser, students
# Create your views here.
def registeruser(req):
    context = {}
    if(req.method=='GET'):
        return  render(req,'register.html')
    else:
        myuser.objects.create(name=req.POST['name'],password=req.POST['password'])
        user=myuser.objects.all()
        return redirect('/login',{'users':user})
    
def login(request):
    context={}
    if(request.method=='GET'):
        context['users']=myuser.objects.all()
        return render(request, 'login.html',context)
    else:
        username=request.POST['name']
        password=request.POST['password']
    
        user= myuser.objects.filter(name=username,password=password)
        if(len(user)>0):
            user=user[0]
        
        if(user):
            return redirect('/home')

        else:
            context['errormsg']='invalid user.'
            return render(request, 'login.html', context)

def home(request):
    return render(request,'home.html')

def addStudent(request):
    if (request.method == 'GET'):
        return render(request, 'addStudent.html')
    else:
        students.objects.create(name=request.POST['name'], track= request.POST['track'])
        student = students.objects.all()
        return redirect('/add', {'student': student})

def updateStudent(request):
    if (request.method == 'GET'):
        return render(request, 'updateStudent.html')
    else:
        stdid = request.POST['stdid']
        newname=request.POST['name']
        newtrack=request.POST['track']
    
        students.objects.filter(id=stdid).update(name=newname, track=newtrack)
        return render(request, 'updateStudent.html')

def deleteStudent(request):
    if (request.method == 'GET'):
        return render(request, 'deleteStudent.html')
    else:
        stdid = request.POST['stdid']
        students.objects.filter(id=stdid).delete()
        return render(request, 'deleteStudent.html')

def selectAll(request):
    context = {}
    context['studs'] = students.objects.all()
    return render(request, 'selectAll.html', context)

def search(request):
    if (request.method == 'GET'):
        return render(request, 'search.html')
    else:
        name = request.POST['name']
        context = {}
        context['studs'] = students.objects.filter(name__icontains=name)
        return render(request, 'search.html', context)