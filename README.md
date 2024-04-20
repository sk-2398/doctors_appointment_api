# Doctors Appointment System

This is a Django web application for managing doctors appointments.

## Installation
Note: Make sure you hae already install Python > 3.8 version.
1. Clone the repository:
   ```
   git clone https://github.com/sk-2398/doctors_appointment_api
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run server:
   ```
   python manage.py runserver
   ```
   This will start the server at http://127.0.0.1:8000.
## API Endpoints
## Render App/Deployed URL: https://doctors-appointment-api-lxb3.onrender.com
You can test this API on Postman or other 
##  1. Add Doctor
- **URL:** `<main-url>/doctors/add/`
- **Method:** POST
- **Request Body:**
  ```
    {
     "name": "Doctor Name",
     "specialty": "Doctor Specialty",
     "max_patients_per_day": 10,
     "location": {
       "address": "Doctor Location Address"
     }
    }
  ```
  
## Doctor List
URL: <main-url>/doctors/
Method: GET

## Doctor Detail
URL: <main-url>/doctors/<doctor_id>/
Method: GET

## Doctor Availability
URL: /doctors/<doctor_id>/availability/
Method: GET
Query Parameters:
date: Date in the format YYYY-MM-DD

## Book Appointment
URL: <main-url>/appointments/book/
Method: POST
Request Body:
json
```
    {
      "doctor_id": 1,
      "patient_name": "Patient Name",
      "appointment_time_str": "2024-04-20 10:00:00"
    }
 ```

## Cancel Appointment
URL: <main-url>/appointments/cancel-appointment/
Method: POST
Request Body:
json
```
{
  "appointment_id": 1
}
```

   
