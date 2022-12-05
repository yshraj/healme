from django.shortcuts import render,redirect
from .models import Patient_registration, Doctor_registration, Pharmacy_registration, Diagnostic_registration,Appointment,Medicines,Pharma,Cart,Report,Order
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
	return render(request,'app/index.html')
def appointment(request):
	print(request.POST['service'])
	return render(request,'app/appointment.html',{'service':request.POST['service'],'doctor':request.POST['doctor']})
def doctor(request):
	return render(request,'app/doctor.html')
def diagnostic(request):
	reports=Report.objects.all()
	return render(request,'app/diagnostic.html',{'reports':reports})
def about(request):
	return render(request,'app/about.html')
def dentist(request):
	service="Dentist"
	doctors=Doctor_registration.objects.filter(speciality="Dentist")
	return render(request, 'app/dentist.html',{'service':service,'doctors':doctors})
def gynecologist(request):
	service="Gynecologist"
	doctors=Doctor_registration.objects.filter(speciality="Gynecologist")
	return render(request, 'app/gynecologist.html',{'service':service,'doctors':doctors})
def physiotherapist(request):
	service="Physiotherapist"
	doctors=Doctor_registration.objects.filter(speciality="Physiotherapist")
	return render(request, 'app/physiotherapist.html',{'service':service,'doctors':doctors})
def orthopedist(request):
	service="Orthopedist"
	doctors=Doctor_registration.objects.filter(speciality="Orthopedist")
	return render(request, 'app/orthopedist.html',{'service':service,'doctors':doctors})
def contact(request):
	return render(request,'app/contact.html')
def patientappointment(request):
	patient=Patient_registration.objects.get(pk=request.session['emailpk'])
	appointment=Appointment.objects.filter(patient=patient)
	print(appointment)
	return render(request,'app/patientappointment.html',{'appointment':appointment})
def patient_registration(request):
	if request.method=="POST":
		fname=request.POST["fname"]
		lname=request.POST["lname"]
		email=request.POST["email"]
		gender=request.POST["gender"]
		bloodgroup=request.POST["bloodgroup"]
		dateofbirth=request.POST["dateofbirth"]
		phone=request.POST["phone"]
		password=request.POST["password"]
		address=request.POST["address"]
		Patient_registration.objects.create(fname=fname,lname=lname,email=email,gender=gender,bloodgroup=bloodgroup,dateofbirth=dateofbirth,phone=phone,password=password,address=address)
		msg="Registration Successful"
		return render(request,'app/login.html',{'msg':msg})
	else:
		return render(request,'app/patient_registration.html')

def login(request):
	if request.method=="POST":
		print(request.POST['email'])
		print(request.POST['password'])
		p=Patient_registration.objects.filter(email=request.POST['email'],password=request.POST['password'])

		if p:
			print(p[0].fname)
			request.session['fname']=p[0].fname
			request.session['lname']=p[0].lname
			request.session['emailpk']=p[0].pk
			return render(request,'app/index.html',{'p':p[0]})
		else:
			error="Username or Password is incorrect"
			return render(request,'app/login.html',{'error':error})	
	else:
		return render(request,'app/login.html')


def logout(request):
	try:
		del request.session['fname']
		return render(request,'app/index.html')
	except:
		pass


def doctor_registration(request):

	if request.method=="POST":
		fname=request.POST["fname"]
		lname=request.POST["lname"]
		email=request.POST["email"]
		gender=request.POST["gender"]
		speciality=request.POST["speciality"]
		fees=request.POST["fees"]
		workingdays=request.POST["workingdays"]
		morningtime=request.POST["morningtime"]
		eveningtime=request.POST["eveningtime"]
		experience=request.POST["experience"]
		password=request.POST["password"]
		image=request.POST['image']
		address=request.POST["address"]
		Doctor_registration.objects.create(fname=fname,lname=lname,email=email,gender=gender,speciality=speciality,fees=fees,workingdays=workingdays,morningtime=morningtime,eveningtime=eveningtime,experience=experience,password=password,image=image,address=address)
		return render(request,'app/doctorlogin.html')
	else:
		return render(request,'app/doctor_registration.html')

def doctorlogin(request):
	try:
		if not request.session['fname']:
			pass
		else:
			msg="Please Logout"
			return render(request,'app/index.html',{'msg':msg})
	except:
		if request.method=="POST":
			print(request.POST['email'])
			print(request.POST['password'])
			d=Doctor_registration.objects.filter(email=request.POST['email'],password=request.POST['password'])

			if d:
				print(d[0].fname)
				request.session['fname']=d[0].fname
				request.session['emailpk']=d[0].pk
				return render(request,'app/doctorhome.html',{'d':d[0]})
			else:
				error="Username or Password is incorrect"
				return render(request,'app/doctorlogin.html',{'error':error})	
		else:
			return render(request,'app/doctorlogin.html')
		#return render(request,'app/doctorlogin.html')
def doctorlogout(request):
	try:
		del request.session['fname']
		return render(request,'app/doctorhome.html')
	except:
		pass 


def doctorhome(request):
	return render(request,'app/doctorhome.html')

def pharmacy_registration(request):
	if request.method=="POST":
		fname=request.POST["fname"]
		lname=request.POST["lname"]
		email=request.POST["email"]
		storename=request.POST["storename"]
		mobile=request.POST["mobile"]
		password=request.POST["password"]
		address=request.POST["address"]
		Pharmacy_registration.objects.create(fname=fname,lname=lname,email=email,storename=storename,mobile=mobile,password=password,address=address)
		return render(request,'app/pharmacylogin.html')
	else:
		return render(request,'app/pharmacy_registration.html')

def pharmacylogin(request):

	if request.method=="POST":
		print(request.POST['email'])
		print(request.POST['password'])
		ph=Pharmacy_registration.objects.filter(email=request.POST['email'],password=request.POST['password'])

		if ph:
			print(ph[0].fname)
			request.session['fname']=ph[0].fname
			request.session['emailpk']=ph[0].pk
			return render(request,'app/pharmacyhome.html',{'ph':ph[0]})
		else:
			error="Username or Password is incorrect"
			return render(request,'app/pharmacylogin.html',{'error':error})	
	else:
		return render(request,'app/pharmacylogin.html')




def pharmacylogout(request):
	try:
		del request.session['fname']
		return render(request,'app/pharmacyhome.html')
	except:
		pass

def diagnostic_registration(request):
	if request.method=="POST":
		fname=request.POST["fname"]
		lname=request.POST["lname"]
		email=request.POST["email"]
		labname=request.POST["labname"]
		mobile=request.POST["mobile"]
		password=request.POST["password"]
		address=request.POST["address"]
		Diagnostic_registration.objects.create(fname=fname,lname=lname,email=email,labname=labname,mobile=mobile,password=password,address=address)
		return render(request,'app/diagnosticlogin.html')
	else:
		return render(request,'app/diagnostic_registration.html')

def diagnosticlogin(request):
	try:
		if not request.session['fname']:
			pass
		else:
			msg="Please Logout"
			return render(request,'app/index.html',{'msg':msg})
	except:
			if request.method=="POST":
				print(request.POST['email'])
				print(request.POST['password'])
				da=Diagnostic_registration.objects.filter(email=request.POST['email'],password=request.POST['password'])

				if da:
					print(da[0].fname)
					request.session['fname']=da[0].fname
					return render(request,'app/diagnostichome.html',{'da':da[0]})
				else:
					error="Username or Password is incorrect"
					return render(request,'app/diagnosticlogin.html',{'error':error})	
			else:
				return render(request,'app/diagnosticlogin.html')

def diagnosticlogout(request):
	try:
		del request.session['fname']
		return render(request,'app/diagnostichome.html')
	except:
		pass


def diagnostichome(request):
	return render(request,'app/diagnostichome.html')



def doctorappointment(request):
	doctor=Doctor_registration.objects.get(pk=request.session['emailpk'])
	myappointment=Appointment.objects.filter(doctor=doctor)
	print(myappointment)
	return render(request,'app/doctorappointment.html',{'myappointment':myappointment})

def doctorprescription(request):
	doctor=Doctor_registration.objects.get(email=request.session['emailpk'])
	print("Doctor : ",doctor)
	appointment=Appointment.objects.filter(doctor=doctor)
	return render(request,'app/doctorprescription.html',{'appointment':appointment})

def doctorreport(request):
	doctor=Doctor_registration.objects.get(email=request.session['emailpk'])
	print("Doctor : ",doctor)
	report=Appointment.objects.filter(doctor=doctor)
	return render(request,'app/doctorreport.html',{'report':report})

def doctorrating(request):
		return render(request,'app/doctorrating.html')

def book(request):
	print(request.POST['doctor'])
	patient=Patient_registration.objects.get(pk=request.session['emailpk'])
	doctor=Doctor_registration.objects.get(email=request.POST['doctor'])
	service=request.POST['service']
	phone=request.POST['phone']
	date=request.POST['date']
	time=request.POST['time']
	message=request.POST['message']

	Appointment.objects.create(patient=patient,doctor=doctor,service=service,phone=phone,date=date,time=time,message=message)
	msg="Your Booking Is Confirmed"
	return render(request,'app/index.html',{'msg':msg})
def send_medicine(request):
	email=request.POST['email']
	medicine=request.POST['medicine']
	rec=[email,]
	subject="Medicine Details"
	message="Your Medicine Details Are : "+medicine
	email_from=settings.EMAIL_HOST_USER
	send_mail(subject,message,email_from,rec)
	return render(request,'app/doctorhome.html')

def pharmacy(request):
	pharmas=Pharma.objects.all()
	return render(request,'app/pharmacy.html',{'pharmas':pharmas})

def cart(request,pk1):
	pharma=Pharma.objects.get(pk=pk1)
	patient=Patient_registration.objects.get(pk=request.session['emailpk'])
	app=Appointment.objects.filter(patient=patient)
	cart=Cart.objects.filter(pharma=pharma,patient=patient)
	if cart:
		error="Medicine Already In Cart"
		pharmas=Pharma.objects.all()
		return render(request,'app/pharmacy.html',{'pharmas':pharmas,'error':error})
	else:
		Cart.objects.create(patient=patient,pharma=pharma)
		ph=Cart.objects.filter(patient=request.session['emailpk'])
		
		return render(request,'app/cart.html',{'ph':ph})


def addtocart(request):
	ph=Cart.objects.filter(patient=request.session['emailpk'])
	msg="Your Order Is Confirmed"
	return render(request,'app/cart.html',{'ph':ph,'msg':msg})

def pharmacyhome(request):
	return render(request,'app/pharmacyhome.html')

def pharmacyorder(request):
	o=Order.objects.all()
	return render(request,'app/pharmacyorder.html',{'o':o})

def medicineorder(request):
	return render(request,'app/medicineorder.html')

def addmedicines(request):
	return render(request,'app/addmedicines.html')

def order(request):	
	return render(request,'app/index.html',{'msg':msg})

def diagnosticappointment(request):
	return render(request,'app/diagnosticappointment.html')

def pdappointment(request):
	return render(request,'app/pdappointment.html',{'reports':request.POST['reports']})
	
def reportbooking(request):
	print(request.POST['reports'])
	patient=Patient_registration.objects.get(pk=request.session['emailpk'])
	reports=Report.objects.get(reportbooking=request.POST['reports'])
	date=request.POST['date']
	time=request.POST['time']
	message=request.POST['message']

	Reportbooking.objects.create(patient=patient,reports=reports,date=date,time=time,message=message)
	msg="Your Booking Is Confirmed"
	return render(request,'app/index.html',{'msg':msg})


def confirm_order(request,pk):
	
	cart=Cart.objects.get(pk=pk)
	patient=Patient_registration.objects.get(pk=cart.patient.pk)
	pharma=Pharma.objects.get(pk=cart.pharma.pk)
	qty=2
	Order.objects.create(patient=patient,pharma=pharma,qty=qty)
	cart.delete()
	ph=Cart.objects.filter(patient=request.session['emailpk'])
	return render(request,'app/cart.html',{'ph':ph})