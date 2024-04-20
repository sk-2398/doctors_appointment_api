from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Doctor, Appointment, Location
from datetime import datetime
from rest_framework import status

@api_view(['POST'])
def add_doctor(request):
    try:
        location_data = request.data.get('location', {})
        location, _ = Location.objects.get_or_create(address=location_data.get('address'))

        doctor = Doctor.objects.create(
            name=request.data.get('name'),
            specialty=request.data.get('specialty'),
            max_patients_per_day=request.data.get('max_patients_per_day'),
            location=location
        )
        
        return JsonResponse({"message": "Doctor added successfully", "doctor_id": doctor.id})
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def doctor_list(request):
    try:
        doctors = Doctor.objects.all()
        data = []
        for doctor in doctors:
            doctor_data = {
                "id": doctor.id,
                "name": doctor.name,
                "specialty": doctor.specialty,
                "location": doctor.location.address
            }
            data.append(doctor_data)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def doctor_detail(request, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        data = {"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty}
        return JsonResponse(data)
    except Doctor.DoesNotExist:
        return JsonResponse({"error": "Doctor not found"}, status=404)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def doctor_availability(request, doctor_id):
    try:
        date_str = request.GET.get('date')
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        doctor = Doctor.objects.get(id=doctor_id)
        if doctor:
            appointments = Appointment.objects.filter(doctor=doctor, appointment_time__date=date)
            available_slots = doctor.max_patients_per_day - appointments.count()
            doctor_data = {
                "id": doctor.id,
                "name": doctor.name,
                "specialty": doctor.specialty,
                "location": doctor.location.address,
                "available_slots": available_slots
            }
            return JsonResponse(doctor_data)
        else:
            return JsonResponse({"error": "Doctor not found"}, status=404)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def book_appointment(request):
    try:
        doctor_id = request.data.get('doctor_id')
        patient_name = request.data.get('patient_name')
        appointment_time_str = request.data.get('appointment_time_str')
        appointment_time = datetime.strptime(appointment_time_str, "%Y-%m-%d %H:%M:%S")
        
        doctor = Doctor.objects.get(id=doctor_id)

        # Check doctor availability
        appointments = Appointment.objects.filter(doctor=doctor, appointment_time__date=appointment_time.date())
        if appointments.count() >= doctor.max_patients_per_day:
            return JsonResponse({"error": "Doctor is not available"}, status=400)

        # Book the appointment
        Appointment.objects.create(doctor=doctor, patient_name=patient_name, appointment_time=appointment_time)
        return JsonResponse({"message": "Appointment booked successfully"})
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def cancel_appointment(request):
    try:
        appointment_id = request.data.get('appointment_id')
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.delete()
        return JsonResponse({"message": "Appointment cancelled successfully"})
    except Appointment.DoesNotExist:
        return JsonResponse({"error": "Appointment not found"}, status=404)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
