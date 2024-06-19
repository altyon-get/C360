from django.http import HttpResponse
from django.shortcuts import render

def home(response):
    return render(response, 'index.html')

def about(response):
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
    return render(response,'about.html',data)

def courseDetails(request,id):
    return HttpResponse(id)