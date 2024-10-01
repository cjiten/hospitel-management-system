from django.shortcuts import render, redirect
from Auth.decorators import org_user_login_required
from DoctorManagement.models import DoctorManagement
from django.contrib import messages

# Create your views here.

@org_user_login_required
def DoctorView(request):
    Doctors = DoctorManagement.objects.all()[:100]
    # set up search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            Doctors = DoctorManagement.objects.filter(name__icontains=keyword)
    data = {
        'Doctors': Doctors,
    }
    return render(request, 'DoctorManagement/DoctorView.html', data)

@org_user_login_required
def DoctorAddView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        speciality = request.POST.get('speciality')
        phone = request.POST.get('phone')
        fee = request.POST.get('fee')
        address = request.POST.get('address')
        create_doctor = DoctorManagement.objects.create(name=name, speciality=speciality, phone=phone, fee=fee, address=address)
        create_doctor.save()
        messages.success(request, 'Doctor Added Successfully')
    return redirect('DoctorView')

@org_user_login_required
def DoctorUpdateView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        speciality = request.POST.get('speciality')
        phone = request.POST.get('phone')
        fee = request.POST.get('fee')
        address = request.POST.get('address')
        update_doctor = DoctorManagement.objects.get(pk=id)
        update_doctor.name = name
        update_doctor.speciality = speciality
        update_doctor.phone = phone
        update_doctor.fee = fee
        update_doctor.address = address
        update_doctor.save()
        messages.success(request, 'Doctor Updated Successfully')
    return redirect('DoctorView')

@org_user_login_required
def DoctorDeleteView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete_doctor = DoctorManagement.objects.get(pk=id)
        delete_doctor.delete()
        messages.info(request, 'Doctor Permanently Deleted')
    return redirect('DoctorView')