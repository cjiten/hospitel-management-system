from django.urls import path
from TreatmentManagement import views

urlpatterns = [
    path('', views.TreatmentView, name='TreatmentView'),
    path('add/', views.TreatmentAddView, name='TreatmentAddView'),
    path('update/', views.TreatmentUpdateView, name='TreatmentUpdateView'),
    path('delete/', views.TreatmentDeleteView, name='TreatmentDeleteView'),

    path('plan/', views.TreatmentPlanView, name='TreatmentPlanView'),
    path('plan/add/', views.TreatmentPlanAddView, name='TreatmentPlanAddView'),
    path('plan/update/', views.TreatmentPlanUpdateView, name='TreatmentPlanUpdateView'),
    path('plan/delete/', views.TreatmentPlanDeleteView, name='TreatmentPlanDeleteView'),
]