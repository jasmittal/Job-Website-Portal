from django.shortcuts import render, redirect
from .models import Job, Application
from django.contrib.auth.decorators import login_required

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        resume = request.FILES['resume']
        Application.objects.create(job=job, applicant=request.user, resume=resume)
        return redirect('job_list')
    return render(request, 'jobs/apply_job.html', {'job': job})