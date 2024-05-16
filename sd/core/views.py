from django.shortcuts import render , HttpResponseRedirect
from  .forms import StudentReg
from .models import student
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            st = fm.cleaned_data['standard']
            sm = fm.cleaned_data['stream']
            # fm.save()
            reg = student(name=nm , email=em , standard = st , stream = sm)
            reg.save()
            fm = StudentReg()
    else:
        fm = StudentReg()
    stud = student.objects.all()
    return render(request , 'addshow.html', {'form':fm , 'stu':stud})


def update_data(request , id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        fm = StudentReg(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = student.objects.get(pk=id)
        fm = StudentReg(instance=pi)
    return render(request , 'updates.html' , {'form':fm})

def delete_data(request , id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
