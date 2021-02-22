from django.db import models

# Create your models here.


class school(models.Model):
    schoolname=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    class Meta:
        abstract=True
class student(school):
    sname = models.CharField(max_length=100)
    srolno = models.IntegerField()
    smarks = models.IntegerField()
    saddress = models.CharField(max_length=100)
    email = models.EmailField(max_length=45)

class teacher(school):
    tname = models.CharField(max_length=100)
    tsalary= models.IntegerField()
    tcity = models.CharField(max_length=20)
    saddress = models.CharField(max_length=100)

class attendant(school):
    aname = models.CharField(max_length=100)
    asalary= models.IntegerField()
    tcity = models.CharField(max_length=20)
    saddress = models.CharField(max_length=100)


    