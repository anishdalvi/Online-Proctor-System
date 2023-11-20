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

from usersite.forms import admissionForm,personalinfoForm,academicForm, currentSemForm, SubjectForm
from usersite.models import admission as admission2
from usersite.models import Semester as semester2
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
        semester1 = semester2.objects.filter(user=request.user).first()
        
        form = admissionForm(request.POST, instance = admission1)
        semesterForm = currentSemForm(request.POST, instance=semester1)

        if form.is_valid() and semesterForm.is_valid():
          print(semesterForm.cleaned_data)

          admission = form.save(commit=False)
          semester = semesterForm.save(commit=False)

          admission.user = user
          semester.user = user

          admission.save()
          semester.save()

          print("Form Saved Admission")


        return redirect("personalinfo")

  else:
        admission1=admission2.objects.filter(user=request.user).first()
        semester1 = semester2.objects.filter(user=request.user).first()
        #print(admission2)
        if not admission1 and semester1:
              form = admissionForm()
              semesterForm = currentSemForm()
        
        else:
          form = admissionForm(instance=admission1)
          semesterForm = currentSemForm(instance=semester1)
        print("Hello else Loaded Admission")
        return render(request, 'admission.html', {'form': form, 'admission1': admission1, 'semesterForm': semesterForm, 'semester1': semester1})
        
  return render(request, 'admission.html', context={'form': form, 'admission1': admission1, 'semesterForm': semesterForm, 'semester1': semester1})



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
        print("Hello else Loaded Personal Info")
        return render(request, 'personalinfo.html', {'form': form, 'personalinfo1': personalinfo1})

  return render(request, 'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})




@login_required
def academic(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      print("POST request received!")
      print(request)
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
    print("Else method not post academic")
    academic1 = academic2.objects.filter(user=request.user).first()
    semester1 = semester2.objects.filter(user=request.user).first()

    current_sem = semester1.current_sem if semester1 else None
    previous_semesters = range(1, current_sem)

    number_subject = 6;
    # print(current_sem)
    if not academic1:
      print("if not academic1")
      form = academicForm()

    else:
      form = academicForm(instance=academic1)
      print("Hello else Loaded Academic")
      return render(request, 'academic.html', {'form': form, 'academic1': academic1, 'current_sem': current_sem, 'previous_semesters': previous_semesters, 'number_subject': number_subject})

    return render(request, 'academic.html', context={'form': form, 'academic1': academic1})




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



