from django.shortcuts import render
from portfolio_app import models
# Create your views here.
def index(request):
    skills =  models.skills.objects.all()
    print("\n\n\n")
    for resume in models.Resume.objects.all():
        resume = resume.resume_file
    
    return render(request, "folio/index.html", context={'resume': resume, 'skills': skills})