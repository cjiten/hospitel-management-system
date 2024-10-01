from django.shortcuts import render, redirect
from Auth.decorators import org_user_login_required
from Auth.models import AuthUser
from GeneralManagement.models import HospitalDetail
from PatientManagement.models import PatientManagement
from AppointmentManagement.models import AppointmentManagement
from TreatmentManagement.models import TreatmentManagement
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

@org_user_login_required
def DashView(request):
    Patients = PatientManagement.objects.all()


    appointments = AppointmentManagement.objects.all()
    appointments_fee_total = sum(appointment.fee for appointment in appointments)

    treatments = TreatmentManagement.objects.all()
    treatments_fee_total = sum(treatment.treatment_deposit for treatment in treatments)
    data = {
        'Patients': Patients,

        'appointments_fee_total': appointments_fee_total,

        'treatments_fee_total': treatments_fee_total,
    }
    return render(request, 'GeneralManagement/DashView.html', data)

@org_user_login_required
def SettingsView(request):
    return render(request, 'GeneralManagement/SettingsView.html')

@org_user_login_required
def HospitalDetailView(request):
    GeneralDetails = get_object_or_404(HospitalDetail)
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        update_detail = HospitalDetail.objects.get(pk=1)
        update_detail.phone = phone
        update_detail.address = address
        update_detail.save()
        messages.success(request, 'Updated Successfully')
        GeneralDetails = get_object_or_404(HospitalDetail)
    data = {
        'GeneralDetails': GeneralDetails,
    }
    return render(request, 'GeneralManagement/HospitalDetailView.html', data)

@org_user_login_required
def AnalyticView(request):
    Patients = PatientManagement.objects.all()
    Appointments = AppointmentManagement.objects.all()
    Treatments = TreatmentManagement.objects.all()


    appointments_online = AppointmentManagement.objects.filter(fee_mode='Online')
    appointments_fee_online = sum(appointment.fee for appointment in appointments_online)

    appointments_offline = AppointmentManagement.objects.filter(fee_mode='Offline')
    appointments_fee_offline = sum(appointment.fee for appointment in appointments_offline)

    appointments_pending = AppointmentManagement.objects.filter(fee_mode='Pending')
    appointments_fee_pending = sum(appointment.fee for appointment in appointments_pending)

    appointments_fee_total_received = appointments_fee_online + appointments_fee_offline - appointments_fee_pending
    appointments_fee_total = appointments_fee_online + appointments_fee_offline + appointments_fee_pending


    treatments_online = TreatmentManagement.objects.filter(treatment_deposit_mode='Online')
    treatments_fee_online = sum(treatment.treatment_deposit for treatment in treatments_online)

    treatments_offline = TreatmentManagement.objects.filter(treatment_deposit_mode='Offline')
    treatments_fee_offline = sum(treatmentt.treatment_deposit for treatmentt in treatments_offline)

    treatments_pending = TreatmentManagement.objects.filter(treatment_deposit_mode='Pending')
    treatments_fee_pending = sum(treatmentt.treatment_deposit for treatmentt in treatments_pending)

    treatments_fee_total_received = treatments_fee_online + treatments_fee_offline - treatments_fee_pending
    treatments_fee_total = treatments_fee_online + treatments_fee_offline + treatments_fee_pending

    data = {
        'Patients': Patients,
        'Appointments': Appointments,
        'Treatments': Treatments,
        'treatments_pending': treatments_pending,

        'appointments_fee_online': appointments_fee_online,
        'appointments_fee_offline': appointments_fee_offline,
        'appointments_fee_pending': appointments_fee_pending,
        'appointments_fee_total_received': appointments_fee_total_received,
        'appointments_fee_total': appointments_fee_total,

        'treatments_fee_online': treatments_fee_online,
        'treatments_fee_offline': treatments_fee_offline,
        'treatments_fee_pending': treatments_fee_pending,
        'treatments_fee_total_received': treatments_fee_total_received,
        'treatments_fee_total': treatments_fee_total,
    }
    return render(request, 'GeneralManagement/AnalyticView.html', data)