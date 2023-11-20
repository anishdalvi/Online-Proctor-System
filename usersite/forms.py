from django.forms import ModelForm
from usersite.models import admission, personalinfo , academic, Subject, Semester
from django.contrib.auth.models import User
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from phonenumber_field.modelfields import PhoneNumberField


class admissionForm(ModelForm):
    class Meta:
        model = admission
        fields = ['procname','surname','name','midname','student_image','rollsem1','rollsem2','rollsem3','rollsem4','rollsem5','rollsem6','rollsem7','rollsem8','year','category','hsc','cet','jee','diploma']



class personalinfoForm(ModelForm):

    # Fnumber = PhoneNumberField(widget=PhoneNumberPrefixWidget())
    # Mnumber = PhoneNumberField(widget=PhoneNumberPrefixWidget())

    class Meta:
        model = personalinfo
        fields = ['dob','birthplace','mothertongue','caste','nameofparent','address','mobnumber','emailid','bloodgroup','disease','fathername','mothername','fatherage','motherage','Faddress','Maddress','Fnumber','Mnumber','Fmail','Mmail','Fqualify','Mqualify','Foccupation','Moccupation','S1name','S2name','S3name','S1age','S2age','S3age', 'S1number','S2number','S3number','S1qualify','S2qualify','S3qualify','S1occupation','S2occupation','S3occupation','income']
        widgets = {
            'Fnumber': PhoneNumberPrefixWidget(),  
            'Mnumber': PhoneNumberPrefixWidget(),  
        }

class academicForm(ModelForm):
    class Meta:
        model = academic
        fields = ['s1s1','s1s2','s1s3','s1s4','s1s5','s1s6']


class currentSemForm(ModelForm):
    class Meta:
        model = Semester
        fields = ['current_year', 'current_sem']

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        # Include other fields from the model if needed
        fields = ['subject_name']
