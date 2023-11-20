from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
# # Create your models here.
# class ToDoList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
#     name = models.CharField(max_length=200)

#     def __str__(self):
# 	       return self.name


# class Item(models.Model):
#     todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     text = models.CharField(max_length=300)
#     complete = models.BooleanField()

#     def __str__(self):
# 	       return self.text

class admission(models.Model):
    COURSES = (
    ('default', 'default'),
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology Engineering', 'Information Technology Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Electronics Engineering', 'Electronics Engineering'),
    )
    branch = models.CharField(max_length=100, choices= COURSES)
    procname = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    midname = models.CharField(max_length=45, blank=True, null=True)
    student_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    rollsem1 = models.IntegerField(blank=True, null=True) 
    rollsem2 = models.IntegerField(blank=True, null=True)
    rollsem3 = models.IntegerField(blank=True, null=True)
    rollsem4 = models.IntegerField(blank=True, null=True)
    rollsem5 = models.IntegerField(blank=True, null=True)
    rollsem6 = models.IntegerField(blank=True, null=True)
    rollsem7 = models.IntegerField(blank=True, null=True)
    rollsem8 = models.IntegerField(blank=True, null=True)
    
    year = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True, default='')
    hsc = models.CharField(max_length=45, blank=True, null=True)
    cet = models.CharField(max_length=45, blank=True, null=True)
    jee = models.CharField(max_length=45, blank=True, null=True)
    diploma = models.CharField(max_length=45, blank=True, null=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)




class personalinfo(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #dob = models.DateField(default=datetime.now, null = True,blank=True) 
    dob = models.CharField(max_length=45,blank=True, null=True)
    birthplace = models.CharField(max_length=45, blank=True, null=True)
    mothertongue = models.CharField(max_length=45, blank=True, null=True)
    caste = models.CharField(max_length=45, blank=True, null=True)
    nameofparent = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=100,default=None,blank=True, null=True)
    #mobnumber = PhoneNumberField(blank=True,null=True)
    mobnumber = models.CharField(max_length=12,blank=True, null=True)
    emailid = models.EmailField(default=None,blank=True, null=True)
    bloodgroup = models.CharField(max_length=45, blank=True, null=True)
    disease = models.CharField(max_length=45,default=None,blank=True, null=True)

    fathername = models.CharField(max_length=45, blank=True, null=True)
    mothername = models.CharField(max_length=45, blank=True, null=True)
    fatherage = models.IntegerField(default=None,blank=True, null=True)
    motherage = models.IntegerField(default=None,blank=True, null=True)
    Faddress = models.TextField(max_length=100,default=None,blank=True, null=True)
    Maddress = models.TextField(max_length=100,default=None,blank=True, null=True)
    Fnumber = PhoneNumberField(blank=True,null=True,unique=True, max_length=10)
    Mnumber = PhoneNumberField(blank=True,null=True,unique=True, max_length=10)
    Fmail = models.EmailField(default=None,blank=True, null=True)
    Mmail = models.EmailField(default=None,blank=True, null=True)
    Fqualify = models.CharField(max_length=45, blank=True, null=True)
    Mqualify = models.CharField(max_length=45, blank=True, null=True)
    Foccupation = models.CharField(max_length=45, blank=True, null=True)
    Moccupation = models.CharField(max_length=45, blank=True, null=True)

    S1name = models.CharField(max_length=45, blank=True, null=True)
    S2name = models.CharField(max_length=45, blank=True, null=True)
    S3name = models.CharField(max_length=45, blank=True, null=True)
    S1age = models.IntegerField(default=0,blank=True, null=True)
    S2age = models.IntegerField(default=0,blank=True, null=True)
    S3age = models.IntegerField(default=0,blank=True, null=True)
    S2number = PhoneNumberField(blank=True,null=True)
    S1number = PhoneNumberField(blank=True,null=True)
    S3number = PhoneNumberField(blank=True,null=True)
    S1qualify = models.CharField(max_length=45, blank=True, null=True)
    S2qualify = models.CharField(max_length=45, blank=True, null=True)
    S3qualify = models.CharField(max_length=45, blank=True, null=True)
    S1occupation = models.CharField(max_length=45, blank=True, null=True)
    S2occupation = models.CharField(max_length=45, blank=True, null=True)
    S3occupation = models.CharField(max_length=45, blank=True, null=True)

    income = models.IntegerField(default=0,blank=True, null=True)



class academic(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    s1s1 = models.IntegerField(blank=True, null=True)
    s1s2 = models.IntegerField(blank=True, null=True)
    s1s3 = models.IntegerField(blank=True, null=True)
    s1s4 = models.IntegerField(blank=True,null=True)
    s1s5 = models.IntegerField(blank=True, null=True)
    s1s6 = models.IntegerField(blank=True, null=True)


class Semester(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    current_year = models.PositiveIntegerField(blank=True,null=True)
    current_sem = models.PositiveIntegerField(blank=True,null=True)
    # Add other fields like semester name, start date, end date, etc.


class Subject(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    # Add other fields related to the subject, such as marks, credits, etc.
