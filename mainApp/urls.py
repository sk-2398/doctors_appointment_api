from django.urls import path
from .views import (
    add_doctor, doctor_list, doctor_detail,
    doctor_availability, book_appointment, cancel_appointment
)

urlpatterns = [
    path('doctors/add/', add_doctor, name='add-doctor'),
    path('doctors/', doctor_list, name='doctor-list'),
    path('doctors/<int:doctor_id>/', doctor_detail, name='doctor-detail'),
    path('doctors/<int:doctor_id>/availability/', doctor_availability, name='doctor-availability'),
    path('appointments/book/', book_appointment, name='book-appointment'),
    path('appointments/cancel-appointment/', cancel_appointment, name='cancel-appointment'),
]
