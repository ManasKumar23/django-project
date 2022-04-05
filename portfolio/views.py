from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.views.decorators.csrf import csrf_exempt
import json
import requests
# Create your views here.
def index(request):
    return HttpResponse("Hello, Welcome to my portfolio")
@csrf_exempt
def job(request):
    if request.method == "GET":
        result = []
        jobs = Job.objects.all()
        # for job in jobs:
        #     data = {
        #         "company":job.company,
        #         "description":job.description
        #     }
        #     result.append(data)
        # print(result)
        return render(request,"portfolio/index.html",{"jobs":jobs})

    if request.method == "POST":
        # print(request.POST.get('company'))
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']
        description = data["description"]
        job = Job (company = company, description = description)
        job.save()
        return HttpResponse(json.dumps("Company added successfully"))






    # if request.method == "DELETE":
    #     body_unicode = request.body.decode('utf-8')
    #     data = json.loads(body_unicode)
    #     company = data["company"]
    #     job = Job.objects.filter(company=company).delete()
    #     return HttpResponse({"Company deleted Successfully."})