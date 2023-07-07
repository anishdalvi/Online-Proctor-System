# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Achievements(models.Model):
    co_cirricullar = models.CharField(max_length=25, blank=True, null=True)
    extra_curricullar = models.CharField(max_length=25, blank=True, null=True)
    sports = models.CharField(max_length=25, blank=True, null=True)
    other = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'achievements'


class AdminsiteStudcred(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mothertongue = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'adminsite_studcred'


""" class admission(models.Model):
    year = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    hsc = models.CharField(max_length=45, blank=True, null=True)
    cet = models.CharField(max_length=45, blank=True, null=True)
    jee = models.CharField(max_length=45, blank=True, null=True)
    diploma = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission' """


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class College(models.Model):
    age = models.IntegerField(db_column='AGE')  # Field name made lowercase.
    credential = models.CharField(max_length=45, blank=True, null=True)
    coll_location = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'college'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Father(models.Model):
    fname = models.CharField(db_column='Fname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fage = models.CharField(db_column='Fage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    faddress = models.CharField(db_column='Faddress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fnumber = models.CharField(db_column='Fnumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fmail = models.CharField(db_column='Fmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fqualify = models.CharField(db_column='Fqualify', max_length=45, blank=True, null=True)  # Field name made lowercase.
    foccupation = models.CharField(db_column='Foccupation', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'father'


class Id(models.Model):
    roll = models.IntegerField()
    name = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'id'


class Index(models.Model):
    value1 = models.CharField(max_length=45)
    value2 = models.CharField(max_length=45, blank=True, null=True)
    value3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index'


class Internals(models.Model):
    sem_no = models.IntegerField(db_column='SEM_No')  # Field name made lowercase.
    sub_1 = models.CharField(db_column='SUB_1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sub_2 = models.CharField(db_column='SUB_2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sub_3 = models.CharField(db_column='SUB_3', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sub_4 = models.CharField(db_column='SUB_4', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sub_5 = models.CharField(db_column='SUB_5', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sub_6 = models.CharField(db_column='SUB_6', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'internals'


class Login(models.Model):
    email = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login'


class Mother(models.Model):
    mname = models.CharField(db_column='Mname', max_length=54, blank=True, null=True)  # Field name made lowercase.
    mage = models.CharField(db_column='Mage', max_length=45, blank=True, null=True)  # Field name made lowercase.
    maddress = models.CharField(db_column='Maddress', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mnumber = models.CharField(db_column='Mnumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mmail = models.CharField(db_column='Mmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mqualify = models.CharField(db_column='Mqualify', max_length=45, blank=True, null=True)  # Field name made lowercase.
    moccupation = models.CharField(db_column='Moccupation', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mother'


class Personal1(models.Model):
    birthdate = models.CharField(max_length=25, blank=True, null=True)
    birthplace = models.CharField(max_length=45, blank=True, null=True)
    mothertongue = models.CharField(max_length=45, blank=True, null=True)
    caste = models.CharField(max_length=45, blank=True, null=True)
    guardian = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    pnumber = models.CharField(db_column='Pnumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=45, blank=True, null=True)
    blood = models.CharField(max_length=45, blank=True, null=True)
    disability = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal1'


class Reg(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    username = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg'


class Regproc(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regproc'


class Roll(models.Model):
    sem1 = models.IntegerField()
    sem2 = models.IntegerField(blank=True, null=True)
    sem3 = models.IntegerField(blank=True, null=True)
    sem4 = models.IntegerField(blank=True, null=True)
    sem5 = models.IntegerField(blank=True, null=True)
    sem6 = models.IntegerField(blank=True, null=True)
    sem7 = models.IntegerField(blank=True, null=True)
    sem8 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roll'


class Sem1(models.Model):
    sub1 = models.CharField(max_length=25, blank=True, null=True)
    sub2 = models.CharField(max_length=25, blank=True, null=True)
    sub3 = models.CharField(max_length=25, blank=True, null=True)
    sub4 = models.CharField(max_length=25, blank=True, null=True)
    sub5 = models.CharField(max_length=25, blank=True, null=True)
    sub6 = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem1'


class Sem2(models.Model):
    sub1 = models.CharField(max_length=45, blank=True, null=True)
    sub2 = models.CharField(max_length=45, blank=True, null=True)
    sub3 = models.CharField(max_length=45, blank=True, null=True)
    sub4 = models.CharField(max_length=45, blank=True, null=True)
    sub5 = models.CharField(max_length=45, blank=True, null=True)
    sub6 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem2'


class Sem3(models.Model):
    sub1 = models.CharField(max_length=45, blank=True, null=True)
    sub2 = models.CharField(max_length=45, blank=True, null=True)
    sub3 = models.CharField(max_length=45, blank=True, null=True)
    sub4 = models.CharField(max_length=45, blank=True, null=True)
    sub5 = models.CharField(max_length=45, blank=True, null=True)
    sub6 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem3'


class Sem4(models.Model):
    sub1 = models.CharField(max_length=45, blank=True, null=True)
    sub2 = models.CharField(max_length=45, blank=True, null=True)
    sub3 = models.CharField(max_length=45, blank=True, null=True)
    sub4 = models.CharField(max_length=45, blank=True, null=True)
    sub5 = models.CharField(max_length=45, blank=True, null=True)
    sub6 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem4'


class Sem5(models.Model):
    sub1 = models.CharField(max_length=45, blank=True, null=True)
    sub2 = models.CharField(max_length=45, blank=True, null=True)
    sub3 = models.CharField(max_length=45, blank=True, null=True)
    sub4 = models.CharField(max_length=45, blank=True, null=True)
    sub5 = models.CharField(max_length=45, blank=True, null=True)
    sub6 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem5'


class Sem6(models.Model):
    sub1 = models.CharField(max_length=45, blank=True, null=True)
    sub2 = models.CharField(max_length=45, blank=True, null=True)
    sub3 = models.CharField(max_length=45, blank=True, null=True)
    sub4 = models.CharField(max_length=45, blank=True, null=True)
    sub5 = models.CharField(max_length=45, blank=True, null=True)
    sub6 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem6'


class Sem7(models.Model):
    sub1 = models.CharField(max_length=45, blank=True, null=True)
    sub2 = models.CharField(max_length=45, blank=True, null=True)
    sub3 = models.CharField(max_length=45, blank=True, null=True)
    sub4 = models.CharField(max_length=45, blank=True, null=True)
    sub5 = models.CharField(max_length=45, blank=True, null=True)
    sub6 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem7'


class Sem8(models.Model):
    sub1 = models.CharField(max_length=45, blank=True, null=True)
    sub2 = models.CharField(max_length=45, blank=True, null=True)
    sub3 = models.CharField(max_length=45, blank=True, null=True)
    sub4 = models.CharField(max_length=45, blank=True, null=True)
    sub5 = models.CharField(max_length=45, blank=True, null=True)
    sub6 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sem8'


class Sibling1(models.Model):
    s1name = models.CharField(db_column='S1name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s1gender = models.CharField(db_column='S1gender', max_length=25, blank=True, null=True)  # Field name made lowercase.
    s1age = models.CharField(db_column='S1age', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s1address = models.CharField(db_column='S1address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s1number = models.CharField(db_column='S1number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s1mail = models.CharField(db_column='S1mail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s1qualify = models.CharField(db_column='S1qualify', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s1occupation = models.CharField(db_column='S1occupation', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sibling1'


class Sibling2(models.Model):
    s2name = models.CharField(db_column='S2name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s2gender = models.CharField(db_column='S2gender', max_length=25, blank=True, null=True)  # Field name made lowercase.
    s2address = models.CharField(db_column='S2address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s2age = models.CharField(db_column='S2age', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s2number = models.CharField(db_column='S2number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s2mail = models.CharField(db_column='S2mail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s2qualify = models.CharField(db_column='S2qualify', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s2occupation = models.CharField(db_column='S2occupation', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sibling2'


class Sibling3(models.Model):
    s3name = models.CharField(db_column='S3name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s3gender = models.CharField(db_column='S3gender', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s3age = models.CharField(db_column='S3age', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s3address = models.CharField(db_column='S3address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s3number = models.CharField(db_column='S3number', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s3mail = models.CharField(db_column='S3mail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s3qualify = models.CharField(db_column='S3qualify', max_length=45, blank=True, null=True)  # Field name made lowercase.
    s3occupation = models.CharField(db_column='S3occupation', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sibling3'


class Stud(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    proof = models.CharField(db_column='PROOF', max_length=50)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stud'


class Student(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    proof = models.CharField(db_column='PROOF', max_length=50)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Table2(models.Model):
    value1 = models.CharField(max_length=45)
    value2 = models.CharField(max_length=45, blank=True, null=True)
    value3 = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table2'


class Usere(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    proof = models.CharField(db_column='PROOF', max_length=50)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE')  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usere'
