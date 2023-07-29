from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
#from .models import Admission
#from usersite.models import admission
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from usersite.forms import admissionForm,personalinfoForm,academicForm
from usersite.models import admission as admission2
from usersite.models import personalinfo as personalinfo2
from usersite.models import academic as academic2
from django.contrib.auth.models import User


# Create your views here.

@login_required(login_url='logreg/login')




@login_required
def admission(request):
  
  if request.method == 'POST':
    if  request.user.is_authenticated:

        user = request.user
        print(user)
        admission1 = admission2.objects.filter(user=request.user).first()
       
        
        form = admissionForm(request.POST, instance = admission1)
        if form.is_valid():
          print(form.cleaned_data)
          admission = form.save(commit=False)
          admission.user = user
          admission.save()


        return redirect("personalinfo")
    

        #admission1 = admission2.objects.get(user=2)
        

  else:
        admission1=admission2.objects.filter(user=request.user).first()
        #print(admission2)
        if not admission1:
              form = admissionForm()

        # adm_details=admission_details.objects.filter(user=request.user.id)
        else:
          form = admissionForm(instance=admission1)
          print("Hello else")
          return render(request,'admission.html',{'form':form,'admission1':admission1})
        
  return render(request,'admission.html', context={'form': form , 'admission1': admission1})



@login_required
def personalinfo(request):
  if request.method == 'POST':
    if request.user.is_authenticated:

        user = request.user
        personalinfo1 = personalinfo2.objects.filter(user=request.user).first()
        #print(user)
        form = personalinfoForm(request.POST, instance=personalinfo1)

        if form.is_valid():
          personalinfo = form.save(commit=False)
          personalinfo.user = user
          personalinfo.save()
        
        return redirect("academic")
        #return render(request, 'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})

    else:
        return redirect('unauthorised')

  else:
      personalinfo1 = personalinfo2.objects.filter(user=request.user).first()
       #print(admission2)
      if not personalinfo1:
          form = personalinfoForm()

        # adm_details=admission_details.objects.filter(user=request.user.id)
      else:
        form = personalinfoForm(instance=personalinfo1)
        print("Hello else Personal Info")
        return render(request, 'personalinfo.html', {'form': form, 'personalinfo1': personalinfo1})

  return render(request, 'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})




@login_required
def academic(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      print("POST request received!")
      user = request.user
      print(user , "at Academic Page")
      academic1 = academic2.objects.filter(user=request.user).first()
      form = academicForm(request.POST, instance=academic1)
      print("In Academic View POST")
      if form.is_valid():
        print("Form Valid")
        academic = form.save(commit=False)
        academic.user = user
        academic.save()
        print("Semester Details Saved")

      return redirect('achievementdetails')

    else:
      print("Unauthorized")
      return redirect('unauthorised')

  else:
    print("else method not post")
    academic1 = academic2.objects.filter(user=request.user).first()
    print(academic1)
    if not academic1:
      print("if not academic1")
      form = academicForm()

    else:
      form = academicForm(instance=academic1)
      print("Hello else Academic")
      return render(request, 'academic.html', {'form': form, 'academic1': academic1})

    return render(request, 'academic.html', context={'form': form, 'academic1': academic1})


""" def submit_academic(request):

  if request.method == 'POST':
    
    if request.user.is_authenticated:

      user = request.user
      print(user, "Submitted Academic")
      form = academicForm(request.POST)
      if form.is_valid():
        #print(form.cleaned_data)
        academic = form.save(commit=False)
        academic.user = user
        academic.save()


        return redirect("achievementdetails")
      else:
        return render(request,'academic.html',context = {'form': form}) """


""" def dynamic_table_view(request):
    # Replace this with the actual logic to get the current semester for the user
    current_semester_number = 5
    semesters = Semester.objects.filter(semester_number__lte=current_semester_number)
    subjects = Subject.objects.filter(semester__in=semesters)

    # Create a dictionary to store subjects for each semester
    semester_subjects = {}
    for semester in semesters:
        semester_subjects[semester] = subjects.filter(semester=semester)

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            semester = Semester.objects.get(
                semester_number=current_semester_number)
            subject.semester = semester
            subject.save()
            # Replace 'success_page' with the URL name for the success page
            return redirect('success_page')
    else:
        form = SubjectForm()

    return render(request, 'dynamic_table.html', {
        'form': form,
        'semester_subjects': semester_subjects,
        'current_semester_number': current_semester_number,
    })
 """

@login_required
def achievementdetails(request):
  if not request.user.is_authenticated:
    return redirect('unauthorised')
  else:
    return render(request,'achievements.html')

""" @login_required
def personalinfo(request):
 if not request.user.is_authenticated:
    return redirect('unauthorised')
 else:
    return render(request,'personalinfo.html') """

@login_required
def logout_view(request):
    logout(request)
    return render(request,'logout.html')

def unauthorised(request):
    return render(request,'unauthorised.html')



