from django.db import models
from django.utils import timezone
# Create your models here.
class Patient_registration(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200 , primary_key=True)
	gender=models.CharField(max_length=200)
	bloodgroup=models.CharField(max_length=200)
	dateofbirth=models.CharField(max_length=200)
	phone=models.CharField(max_length=200,default="")
	password=models.CharField(max_length=200)
	address=models.CharField(max_length=400)

	def __str__(self):
		return self.fname

class Doctor_registration(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200, primary_key=True)
	gender=models.CharField(max_length=200)
	speciality=models.CharField(max_length=200)
	fees=models.CharField(max_length=200,default="")
	workingdays=models.CharField(max_length=200,default="")
	morningtime=models.CharField(max_length=200,default="")
	eveningtime=models.CharField(max_length=200,null=True,blank=True)
	experience=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	image=models.ImageField(upload_to='images', max_length=1000,default="")
	address=models.CharField(max_length=400)

	def __str__(self):
		return self.fname

class Pharmacy_registration(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	storename=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	address=models.CharField(max_length=400)

	def __str__(self):
		return self.fname	

class Diagnostic_registration(models.Model):
	fname=models.CharField(max_length=200)
	lname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	labname=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200)
	password=models.CharField(max_length=200)
	address=models.CharField(max_length=400)

	def __str__(self):
		return self.fname	

class Appointment(models.Model):
	patient=models.ForeignKey(Patient_registration,on_delete=models.CASCADE)
	doctor=models.ForeignKey(Doctor_registration,on_delete=models.CASCADE,default="")
	service=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)
	message=models.CharField(max_length=100)

class Medicines(models.Model):
	patient=models.ForeignKey(Patient_registration,on_delete=models.CASCADE)
	pharmacy=models.ForeignKey(Pharmacy_registration,on_delete=models.CASCADE,default="")
	medicines=models.CharField(max_length=100)
	quantity=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	address=models.CharField(max_length=100)

class Pharma(models.Model):
	image=models.ImageField(upload_to='images', max_length=1000,default="")
	name=models.CharField(max_length=200)
	price=models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Cart(models.Model):
	patient=models.ForeignKey(Patient_registration,on_delete=models.CASCADE)
	pharma=models.ForeignKey(Pharma,on_delete=models.CASCADE)
		
class Order(models.Model):
	patient=models.ForeignKey(Patient_registration,on_delete=models.CASCADE)
	pharma=models.ForeignKey(Pharma,on_delete=models.CASCADE)
	qty=models.CharField(max_length=100)
	order_date=models.DateTimeField(default=timezone.now)

class Report(models.Model):
	reportname=models.CharField(max_length=100)
	reportdetail1=models.CharField(max_length=100)
	reportdetail2=models.CharField(max_length=100)
	reportdetail3=models.CharField(max_length=300)
	reportdetail4=models.CharField(max_length=100)
	reportdetail5=models.CharField(max_length=300)
	price=models.CharField(max_length=100)

	def __str__(self):
		return self.reportname

class Reportbooking(models.Model):
	patient=models.ForeignKey(Patient_registration,on_delete=models.CASCADE)
	reports=models.ForeignKey(Report,on_delete=models.CASCADE,default="")
	date=models.CharField(max_length=100)
	time=models.CharField(max_length=100)
	message=models.CharField(max_length=100)
