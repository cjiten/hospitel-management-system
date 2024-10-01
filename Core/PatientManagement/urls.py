from django.urls import path
from PatientManagement import views

urlpatterns = [
    path('', views.PatientView, name='PatientView'),
    path('add/', views.PatientAddView, name='PatientAddView'),
    path('update/', views.PatientUpdateView, name='PatientUpdateView'),
    path('delete/', views.PatientDeleteView, name='PatientDeleteView'),

    path('<slug:slug>/', views.PatientDetailsView, name='PatientDetailsView'),
]
