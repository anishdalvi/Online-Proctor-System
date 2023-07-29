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

#from usersite.models import admission1
#from django.contrib.auth.forms import Authentication

# Create your views here.

@login_required(login_url='logreg/login')



# """ def admission(request):
#   if not request.user.is_authenticated:
#     return redirect('unauthorised')
#   else:
#      if request.method == 'POST':
#       year = request.POST.get('year')
#       category = request.POST.get('category')
#       hsc = request.POST.get('hsc')
#       cet = request.POST.get('cet')
#       jee = request.POST.get('jee')
#       diploma = request.POST.get('diploma')
#       print(year,category,hsc,cet,jee)
#       da = admission(year=year,category=category,hsc=hsc,cet=cet,jee=jee,diploma=diploma)
#       da.save()

#   return render(request,'admission.html')  """

# parenthesis

# def admission1(request):
  # n=''
  # if request.method == 'POST':
  #     year = request.POST.get('year')
  #     category = request.POST.get('category')
  #     hsc = request.POST.get('hsc')
  #     cet = request.POST.get('cet')
  #     jee = request.POST.get('jee')
  #     diploma = request.POST.get('diploma')
  #     print(year,category,hsc,cet,jee)
  #     da = admission1(year=year,category=category,hsc=hsc,cet=cet,jee=jee,diploma=diploma)
  #     da.save()
  #     n='Data Inserted'


  # return render(request,'admission.html',{'n':n})



# square brackets

#  if request.method == 'POST':
#       year = request.POST['year']
#       category = request.POST['category']
#       hsc = request.POST['hsc']
#       cet = request.POST['cet']
#       jee = request.POST['jee']
#       diploma = request.POST['diploma']

# Vishal

#if request.user.is_authenticated:
    #    user = request.user
   #     form = OapForm()
  #      oaps = Oap.objects.filter(user = user)
 #       return render(request , 'oap.html' , context={'form' : form , 'oaps' : oaps})

@login_required
def admission(request):
  """ if  request.user.is_authenticated:

      user = request.user
      print(user)
      form = admissionForm()
      #admission1 = admission2.objects.get(user=2)
      try:
        admission1 = admission2.objects.filter(user=user).latest('pk')
      except:
        admission1 = admission2.objects.filter(user=user)
      #admission1 = admission2.objects.all()

      return render(request,'admission.html', context={'form': form , 'admission1': admission1})
      #return render(request,'admission.html', context={'form': form)

  else:

    return redirect('unauthorised') """
  if request.method == 'POST':
    if  request.user.is_authenticated:

        user = request.user
        print(user)
        admission1 = admission2.objects.filter(user=request.user).first()
        #form = admissionForm()
        
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


""" @login_required
def submit_admission(request):

    if request.user.is_authenticated:

      user = request.user
      #print(user)
      form = admissionForm(request.POST)
      if form.is_valid():
        print(form.cleaned_data)
        admission = form.save(commit=False)
        admission.user = user
        admission.save()


        return redirect("personalinfo")
      else:
        return render(request,'admission.html',context = {'form': form}) """



""" @login_required
def personalinfo(request):
 if not request.user.is_authenticated:
    return redirect('unauthorised')
 else:
    user = request.user
    print(user)
    form = personalinfoForm()
    try:
      personalinfo1 = personalinfo2.objects.filter(user=user).latest('pk')
    except:
      personalinfo1 = personalinfo2.objects.filter(user=user)

    return render(request,'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1}) """


""" @login_required   BY rishabh
def personalinfo(request):

  if  request.user.is_authenticated:

      user = request.user
      print(user)
      form = personalinfoForm()
      this_user = User.objects.get(username=user)
      print(this_user)
      personalinfo1 = personalinfo2.objects.filter(user=this_user)
      print(personalinfo1)
      return render(request,'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})
      # return render(request,'personalinfo.html', context={'form': form})

  else:
      return redirect('unauthorised')



@login_required
def submit_personalinfo(request):
      try:
        if request.user.is_authenticated:

          user = request.user
          # print(user)
          # print(user)
          form = personalinfoForm(request.POST)
          try:
            if request.method == 'POST':
              print(5)
              # print(user)
              print(form.cleaned_data)
              personalinfo = form.save(commit=False)
              personalinfo.user = user
              personalinfo.save()
              print(1)
              return redirect('academic')

          except:
            print(4)
            if form.errors:
              for error in form.errors:
                print("Error:  ",error)

            return redirect('academic')

          else:
            print(2)
            return redirect('personalinfo')

      except Exception:
        print(Exception)
        print(3) """


""" This is till Sem 4 """

""" @login_required
def personalinfo(request):
  if  request.user.is_authenticated:

      user = request.user
      #print(user)
      form = personalinfoForm()
      try:
        print(1)
        personalinfo1 = personalinfo2.objects.filter(user=user).latest('pk')
      except:
        print(2)
        personalinfo1 = personalinfo2.objects.filter(user=user)
      return render(request,'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})

  else:
      return redirect('unauthorised')


def submit_personalinfo(request):

    if request.user.is_authenticated:

      user = request.user
      print(user,"submitted personalinfo")
      form = personalinfoForm(request.POST)
      print("after form",user)
      if form.is_valid():
        print('Form Valid')
        #print(form.cleaned_data)
        personalinfo = form.save(commit=False)
        personalinfo.user = user
        personalinfo.save()


        return redirect("academic")
      else:
        
        print("Form skipped")
        return render(request,'personalinfo.html',context = {'form': form}) """


""" This is till Sem 4 end """


@login_required
def personalinfo(request):
  if request.method == 'POST':
    if request.user.is_authenticated:

        user = request.user
        personalinfo1 = personalinfo2.objects.filter(user=request.user).first()
        #print(user)
        form = personalinfoForm(request.POST, instance=personalinfo1)

        if form.is_valid():
          personalinfo1 = form.save(commit=False)
          personalinfo1.user = user
          personalinfo1.save()
        
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
        print("Hello else")
        return render(request, 'personalinfo.html', {'form': form, 'personalinfo1': personalinfo1})

  return render(request, 'personalinfo.html', context={'form': form, 'personalinfo1': personalinfo1})




@login_required
def academic(request):
  if  request.user.is_authenticated:

      user = request.user
      print(user , "at Academic Page")
      form = academicForm()
      try:
        academic1 = academic2.objects.filter(user=user).latest('pk')
      except:
        academic1 = academic2.objects.filter(user=user)
      return render(request,'academic.html', context={'form': form, 'academic1': academic1})

  else:
      return redirect('unauthorised')


def submit_academic(request):

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
        return render(request,'academic.html',context = {'form': form})




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



