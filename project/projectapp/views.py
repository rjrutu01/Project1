from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from projectapp.models import Client,Project
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='GET':
            return render(request,'register.html')
    else:
            username=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            password=request.POST['password']
            confirm_password=request.POST['confirm_password']
            
            if password==confirm_password:
                u=User.objects.create(username=username,email=email,first_name=first_name,last_name=last_name)
                u.set_password(password)
                u.save()
                return redirect('/')
            else:
                context={}
                context['error']='Password and Confirm password does not match'
                return render(request,'sign_up.html',context)
            
def sign_in(request):
    if request.method =='GET':
        return render(request,'sign_in.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context={}
            context['error']='Username and password not found'
            return render(request,'sign_in.html',context)

def client(request):
    if request.method =='GET':
        return render(request,'client.html')
    else:
        name=request.POST['name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        c=Client.objects.create(name=name,email=email,phone_number=phone_number)
        c.save()
        return redirect('/read_client')
    
def read_client(request):
    c=Client.objects.all()
    context={}
    context['data']=c
    return render(request,'read_client.html',context)

def delete_client(request,rid):
    p=Client.objects.filter(id=rid)
    p.delete()
    return redirect('/read_client')

def project(request):
    if request.method =='GET':
        return render(request,'project.html')
    else:
        name=request.POST['name']
        description=request.POST['description']
        client=request.POST['client']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        p=Project.objects.create(name=name,description=description,client=client,start_date=start_date,end_date=end_date)
        p.save()
        return redirect('/read_project')

def read_project(request):
    p=Project.objects.all()
    context={}
    context['data']=p
    return render(request,'read_project.html',context)
        

