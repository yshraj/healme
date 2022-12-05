from django.contrib import admin

# Register your models here.
from .models import Patient_registration,Doctor_registration,Pharmacy_registration,Diagnostic_registration,Appointment,Medicines,Pharma,Cart,Report,Order,Reportbooking
admin.site.register(Patient_registration)
admin.site.register(Doctor_registration)
admin.site.register(Pharmacy_registration)
admin.site.register(Diagnostic_registration)
admin.site.register(Appointment)
admin.site.register(Medicines)
admin.site.register(Pharma)
admin.site.register(Cart)
admin.site.register(Report)
admin.site.register(Order)
admin.site.register(Reportbooking)