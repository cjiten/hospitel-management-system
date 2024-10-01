from django.urls import path
from AppointmentManagement import views

urlpatterns = [
    path('', views.AppointmentView, name='AppointmentView'),
    path('add/', views.AppointmentAddView, name='AppointmentAddView'),
    path('update/', views.AppointmentUpdateView, name='AppointmentUpdateView'),
    path('delete/', views.AppointmentDeleteView, name='AppointmentDeleteView'),
]