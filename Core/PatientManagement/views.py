from django.shortcuts import render, redirect, get_object_or_404
from PatientManagement.models import PatientManagement
from DoctorManagement.models import DoctorManagement
from AppointmentManagement.models import AppointmentManagement
from TreatmentManagement.models import TreatmentManagement
from django.contrib import messages
from django.core.paginator import Paginator
from Auth.decorators import org_user_login_required

# Create your views here.

@org_user_login_required
def PatientView(request):
    Patients = PatientManagement.objects.order_by('-created_date')[:25]
    Doctors = DoctorManagement.objects.all()
    # set up search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            Patients = PatientManagement.objects.filter(full_name__icontains=keyword)
    # set up pagination
    p = Paginator(PatientManagement.objects.order_by('-created_date'), 25)
    page = request.GET.get('page')
    Pages = p.get_page(page)
    data = {
        'Patients': Patients,
        'Pages': Pages,
        'Doctors': Doctors,
    }
    return render(request, 'PatientManagement/PatientView.html', data)

@org_user_login_required
def PatientAddView(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        care_of = request.POST.get('care_of')
        aadhar = request.POST.get('aadhar')
        dob = request.POST.get('dob')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        doctor_id = request.POST.get('doctor')
        address = request.POST.get('address')
        remark = request.POST.get('remark')
        doctor = DoctorManagement.objects.get(id=doctor_id)
        create_patient = PatientManagement.objects.create(full_name=full_name, care_of=care_of, aadhar=aadhar, dob=dob, sex=sex, phone=phone, doctor=doctor, address=address, remark=remark)
        create_patient.save()
        messages.success(request, 'Patient Added Successfully')
    return redirect('PatientView')

@org_user_login_required
def PatientUpdateView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        full_name = request.POST.get('full_name')
        care_of = request.POST.get('care_of')
        aadhar = request.POST.get('aadhar')
        dob = request.POST.get('dob')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')
        doctor_id = request.POST.get('doctor')
        address = request.POST.get('address')
        remark = request.POST.get('remark')
        doctor = DoctorManagement.objects.get(id=doctor_id)
        update_patient = PatientManagement.objects.get(pk=id)
        update_patient.full_name = full_name
        update_patient.care_of = care_of
        update_patient.aadhar = aadhar
        update_patient.dob = dob
        update_patient.sex = sex
        update_patient.phone = phone
        update_patient.doctor = doctor
        update_patient.address = address
        update_patient.remark = remark
        update_patient.save()
        messages.success(request, 'Patient Updated Successfully')
    return redirect('PatientView')

@org_user_login_required
def PatientDeleteView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete_patient = PatientManagement.objects.get(pk=id)
        delete_patient.delete()
        messages.info(request, 'Patient Permanently Deleted')
    return redirect('PatientView')

@org_user_login_required
def PatientDetailsView(request, slug):
    Patient = get_object_or_404(PatientManagement, pk=slug)
    Appointments = AppointmentManagement.objects.filter(patient=Patient)
    Treatments = TreatmentManagement.objects.filter(treatment_patient=Patient)
    data = {
        'Patient': Patient,
        'Appointments': Appointments,
        'Treatments': Treatments,
    }
    return render(request, 'PatientManagement/PatientDetailsView.html', data)