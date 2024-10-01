from django.urls import path
from GeneralManagement import views

urlpatterns = [
    path('', views.DashView, name="DashView"),
    path('settings/', views.SettingsView, name="SettingsView"),
    path('settings/details/', views.HospitalDetailView, name="HospitalDetailView"),

    path('analytic/', views.AnalyticView, name='AnalyticView')
]
