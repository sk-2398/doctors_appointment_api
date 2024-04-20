from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=255)

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    max_patients_per_day = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    appointment_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
