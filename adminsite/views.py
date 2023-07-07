from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
#from adminsite.models import admission, studcred
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='logreg/login')
def home(request):
    studs=studcred.objects.all()
    if not request.user.is_authenticated:
        return redirect('unauthorised')
    return render(request,'index.html',{'studs':studs})