from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Login(models.Model):
    Loginid=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

class CollegeSuper(models.Model):
    Co_id=models.AutoField(primary_key=True)
    CO_name=models.CharField(max_length=50)
    CO_addrss=models.CharField(max_length=50)
    CO_email=models.CharField(max_length=50)
    CO_pno=models.CharField(max_length=10)

    def __str__(self):
        return self.CO_name

class Student(models.Model):
    S_id=models.AutoField(primary_key=True)        
    S_fname=models.CharField(max_length=30)
    S_mname=models.CharField(max_length=30)
    S_lname=models.CharField(max_length=30)
    S_email=models.CharField(max_length=30)
    SCO=models.ForeignKey(CollegeSuper,on_delete=models.DO_NOTHING)


class mideterm(models.Model):
 domainandtech=models.IntegerField()
 profesethi=models.IntegerField()
 interpersonatl=models.IntegerField()
 presentation=models.IntegerField()
 communication=models.IntegerField()
 taskcompleted=models.IntegerField()
 questionans=models.IntegerField()
 total=models.IntegerField()
 SM=models.ForeignKey(Student,on_delete=models.DO_NOTHING)

class Endterm(models.Model):
 background=models.IntegerField()
 scopeandobj=models.IntegerField()
 implemen=models.IntegerField()
 observa=models.IntegerField()
 domain=models.IntegerField()
 presentation=models.IntegerField()
 communic=models.IntegerField()
 interper=models.IntegerField()
 profess=models.IntegerField()
 qanda=models.IntegerField()
 E_total=models.IntegerField()
 SE=models.ForeignKey(Student,on_delete=models.DO_NOTHING)

