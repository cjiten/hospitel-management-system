from django.urls import path
from DoctorManagement import views

urlpatterns = [
    path('', views.DoctorView, name="DoctorView"),
    path('add/', views.DoctorAddView, name="DoctorAddView"),
    path('update/', views.DoctorUpdateView, name="DoctorUpdateView"),
    path('delete/', views.DoctorDeleteView, name="DoctorDeleteView"),
]
