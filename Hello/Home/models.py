from django.db import models

# Create your models here.

class Employee(models.Model):
    Employee_ID = models.IntegerField(default='SOME STRING')
    First_Name = models.CharField(max_length=100,default='SOME STRING')
    Last_Name = models.CharField(max_length=100, default='SOME STRING')
    Designation = models.CharField(max_length=100,default='SOME STRING')
    Employee_Phoneno = models.IntegerField(default=0)
    Employee_DOB = models.DateTimeField(default=0)

class User_Clients(models.Model):
    Client_ID = models.IntegerField(default='SOME STRING')
    Client_Name = models.CharField(max_length=100,default='SOME STRING')
    Client_Phone = models.IntegerField(default=0)
    Category = models.CharField(max_length=100,default='SOME STRING')

class Contacts(models.Model):
    Contact_ID = models.IntegerField(default=0)
    Client_ID = models.IntegerField(default='SOME STRING')
    Employee_ID = models.IntegerField(default='SOME STRING')
    Admin_ID = models.IntegerField(default='SOME STRING')

class Admin(models.Model):
    Admin_ID = models.IntegerField(default=0)
    Admin_Name = models.CharField(max_length=100, default='SOME STRING')
    Employee_ID = models.IntegerField(default='SOME STRING')

class Projects(models.Model):
    Project_ID = models.IntegerField(default=0)
    Client_ID = models.IntegerField(default='SOME STRING')
    Employee_ID = models.IntegerField(default='SOME STRING')
    Project_Details = models.CharField(max_length=100, default='SOME STRING')
    Strat_Date = models.DateTimeField(default=0)
    Due_Date = models.DateTimeField(default=0)
    Is_completed = models.CharField(max_length=10,default='False')
    Project_Category = models.CharField(max_length=100,default='Some String')

class Transcation_Employee(models.Model):
    Transcation_ID = models.IntegerField(default=0)
    Employee_ID = models.IntegerField(default='SOME STRING')
    Project_ID = models.IntegerField(default=0)
    Transcation_Date = models.DateTimeField(default=0)

class Transcation_Client(models.Model):
    Transcation_ID = models.IntegerField(default=0)
    Client_ID = models.IntegerField(default='SOME STRING')
    Project_ID = models.IntegerField(default=0)
    Transcation_Date = models.DateTimeField(default=0)