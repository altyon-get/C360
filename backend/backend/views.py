from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from service.models import Service

def home(response):
    return render(response, 'index.html')

def about(request):
    serviceData=Service.objects.all().order_by('-service_name')
    data={
        'title': 'A Career is a life',
        'colleges': ['NSUT','DTU'],
        'exams': ['NEET','JEE-MAINS'],
        'courses': ['MBA','BE','MBBS','BSC'],
        'councellers': [
            {'name':'pradeep' , 'phone': 2149832298},
            {'name':'pradeep' , 'phone': 2149832298},
            {'name':'pradeep' , 'phone': 2149832298},
        ],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
        'serviceData':serviceData,
    }
    return render(request,'about.html',data)

def courseDetails(request,id):
    return HttpResponse(id)

def contact(request):
    return HttpResponse('You have submitted the details successfully')

def submitDetails(request):
    print('submitDetials is Called')
    final = 0
    try:
        if request.method=="POST":
            n = request.POST['username']
            m = request.POST['password']
            final = n+m
        return HttpResponseRedirect('/contact')
    except:
        pass

    return render(request,'userForm.html',{'output':final})


def calc(request):
    return render(request,'calc.html')

def submit_operation(request):
    n1=0
    n2=0
    c = 0
    try:
        print('hi')
        n1 = request.POST['num1']
        n2 = request.POST['num2']
        op = request.POST['operation']
        print('incomig:',n1,n2,c)
        if op=='+':
            c = n1+n2
        else:
            c=n1-n2
        
        print(n1,n2,c)
        
    except:
        print('error')
    
    return render(request,'calc.html',{'result':c,'n1':n1,'n2':n2})