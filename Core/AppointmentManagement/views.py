from django.shortcuts import render, redirect
from AppointmentManagement.models import AppointmentManagement
from PatientManagement.models import PatientManagement
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from Auth.decorators import org_user_login_required

# Create your views here.

@org_user_login_required
def AppointmentView(request):
    Appointments = AppointmentManagement.objects.order_by('-created_date_time')[:25]
    # set up search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            Appointments = AppointmentManagement.objects.filter(appointment_id__icontains=keyword)
    # set up pagination
    p = Paginator(AppointmentManagement.objects.order_by('-created_date_time'), 25)
    page = request.GET.get('page')
    Pages = p.get_page(page)
    data = {
        'Appointments': Appointments,
        'Pages': Pages,
    }
    return render(request, 'AppointmentManagement/AppointmentView.html', data)

@org_user_login_required
def AppointmentAddView(request):
    if request.method == 'POST':
        patient_aadhar = request.POST.get('patient_aadhar')
        fee_mode = request.POST.get('fee_mode')
        try:
            if not patient_aadhar.isdigit() or len(patient_aadhar) != 12:
                messages.warning(request, 'Enter a valid Aadhar Number.')
                return redirect('AppointmentView')
       
            patient = PatientManagement.objects.get(aadhar=patient_aadhar)
            now = timezone.now()
            # Extract year, month, day, hour, minute, second
            year = str(now.year)
            month = str(now.month).zfill(2)
            day = str(now.day).zfill(2)
            hour = str(now.hour).zfill(2)
            minute = str(now.minute).zfill(2)
            second = str(now.second).zfill(2)
            prifix = 'AP-'
            # Combine date, time, and unique ID
            appointment_id = f"{prifix}{year}{month}{day}{hour}{minute}{second}"

            if fee_mode == 'Free':
                fee = 0
            else:
                fee = patient.doctor.fee
            create_appointment = AppointmentManagement.objects.create(appointment_id=appointment_id, patient=patient, fee=fee, fee_mode=fee_mode)
            create_appointment.save()
            messages.success(request, 'Appointment Created Successfully')
        except PatientManagement.DoesNotExist:
            messages.warning(request, 'Patient not found.')
            return redirect('AppointmentView')
    return redirect('AppointmentView')

@org_user_login_required
def AppointmentUpdateView(request):
        if request.method == 'POST':
            id = request.POST.get('id')
            fee = request.POST.get('fee')
            fee_mode = request.POST.get('fee_mode')
            update_appointment = AppointmentManagement.objects.get(pk=id)
            update_appointment.fee = fee
            update_appointment.fee_mode = fee_mode
            update_appointment.save()
            messages.success(request, 'Appointment Updated Successfully')
        return redirect('AppointmentView')

@org_user_login_required
def AppointmentDeleteView(request):
    if request.method == 'POST':
        appointment_id = request.POST.get('appointment_id')
        delete_appointment = AppointmentManagement.objects.get(appointment_id=appointment_id)
        delete_appointment.delete()
        messages.info(request, 'Appointment Permanently Deleted')
    return redirect('AppointmentView')