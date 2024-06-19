from django.http import HttpResponse
from django.shortcuts import render

def home(response):
    return render(response, 'index.html')

def about(request):
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
    }
    return render(request,'about.html',data)

def courseDetails(request,id):
    return HttpResponse(id)

def contact(request):
    return HttpResponse('This is contact page')

def submitDetails(request):
    print('submitDetials is Called')
    final = 0
    try:
        if request.method=="POST":
            n = request.POST['username']
            m = request.POST['password']
            final = n+m
    except:
        pass

    return render(request,'userForm.html',{'output':final})
