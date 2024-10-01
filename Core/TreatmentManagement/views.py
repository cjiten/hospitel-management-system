from django.shortcuts import render
from django.shortcuts import render, redirect
from TreatmentManagement.models import TreatmentPlan, TreatmentManagement
from PatientManagement.models import PatientManagement
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone
from Auth.decorators import org_user_login_required

# Create your views here.

@org_user_login_required
def TreatmentPlanView(request):
    TreatmentPlans = TreatmentPlan.objects.order_by('-name')[:25]
    # set up search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            TreatmentPlans = TreatmentPlan.objects.filter(name__icontains=keyword)
    # set up pagination
    p = Paginator(TreatmentPlan.objects.order_by('-name'), 25)
    page = request.GET.get('page')
    Pages = p.get_page(page)
    data = {
        'TreatmentPlans': TreatmentPlans,
        'Pages': Pages,
    }
    return render(request, 'TreatmentManagement/TreatmentPlanView.html', data)

@org_user_login_required
def TreatmentPlanAddView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        create_treatment_plan = TreatmentPlan.objects.create(name=name, cost=cost)
        create_treatment_plan.save()
        messages.success(request, 'Treatment Plan Created Successfully')
        return redirect('TreatmentPlanView')
    return redirect('TreatmentPlanView')

@org_user_login_required
def TreatmentPlanUpdateView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        create_treatment_plan = TreatmentPlan.objects.get(pk=id)
        create_treatment_plan.name = name
        create_treatment_plan.cost = cost
        create_treatment_plan.save()
        messages.success(request, 'Treatment Plan Updated Successfully')
        return redirect('TreatmentPlanView')
    return redirect('TreatmentPlanView')

@org_user_login_required
def TreatmentPlanDeleteView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete_treatment = TreatmentPlan.objects.get(pk=id)
        delete_treatment.delete()
        messages.info(request, 'Treatment Plan Permanently Deleted')
    return redirect('TreatmentPlanView')

@org_user_login_required
def TreatmentView(request):
    Treatments = TreatmentManagement.objects.order_by('-created_date_time')[:25]
    TreatmentPlans = TreatmentPlan.objects.all()
    # set up search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            Treatments = TreatmentManagement.objects.filter(treatment_id__icontains=keyword)
    # set up pagination
    p = Paginator(TreatmentManagement.objects.order_by('-created_date_time'), 25)
    page = request.GET.get('page')
    Pages = p.get_page(page)
    data = {
        'Treatments': Treatments,
        'TreatmentPlans': TreatmentPlans,
        'Pages': Pages,
    }
    return render(request, 'TreatmentManagement/TreatmentView.html', data)

@org_user_login_required
def TreatmentAddView(request):
    if request.method == 'POST':
        patient_aadhar = request.POST.get('patient_aadhar')
        treatment_plan_id = request.POST.get('treatment_plan_id')
        print(treatment_plan_id)
        try:
            if not patient_aadhar.isdigit() or len(patient_aadhar) != 12:
                messages.warning(request, 'Enter a valid Aadhar Number.')
                return redirect('TreatmentView')
       
            treatment_patient = PatientManagement.objects.get(aadhar=patient_aadhar)
            treatment_plan = TreatmentPlan.objects.get(id=treatment_plan_id)
            now = timezone.now()
            # Extract year, month, day, hour, minute, second
            year = str(now.year)
            month = str(now.month).zfill(2)
            day = str(now.day).zfill(2)
            hour = str(now.hour).zfill(2)
            minute = str(now.minute).zfill(2)
            second = str(now.second).zfill(2)
            prifix = 'TM-'
            # Combine date, time, and unique ID
            treatment_id = f"{prifix}{year}{month}{day}{hour}{minute}{second}"
            create_treatment = TreatmentManagement.objects.create(treatment_id=treatment_id, treatment_name=treatment_plan.name, treatment_cost=treatment_plan.cost, treatment_patient=treatment_patient)
            create_treatment.save()
            messages.success(request, 'Treatment Created Successfully')
        except PatientManagement.DoesNotExist:
            messages.warning(request, 'Patient not found.')
            return redirect('TreatmentView')
    return redirect('TreatmentView')

@org_user_login_required
def TreatmentUpdateView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        treatment_id = request.POST.get('treatment_id')
        treatment_stauts = request.POST.get('treatment_stauts')
        treatment_name = request.POST.get('treatment_name')
        treatment_cost = request.POST.get('treatment_cost')
        treatment_deposit = request.POST.get('treatment_deposit')
        treatment_deposit_mode = request.POST.get('treatment_deposit_mode')
        treatment = request.POST.get('treatment')
        update_treatment = TreatmentManagement.objects.get(pk=id)
        update_treatment.treatment_id = treatment_id
        update_treatment.treatment_stauts = treatment_stauts
        update_treatment.treatment_name = treatment_name
        update_treatment.treatment_cost = treatment_cost
        update_treatment.treatment_deposit = treatment_deposit
        update_treatment.treatment_deposit_mode = treatment_deposit_mode
        update_treatment.treatment = treatment
        update_treatment.save()
        messages.success(request, 'Treatment Updated Successfully')
        return redirect('TreatmentView')

@org_user_login_required
def TreatmentDeleteView(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        delete_treatment = TreatmentManagement.objects.get(pk=id)
        delete_treatment.delete()
        messages.info(request, 'Treatment Permanently Deleted')
    return redirect('TreatmentView')