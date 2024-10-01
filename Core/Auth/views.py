from django.shortcuts import render, redirect
from django.contrib import messages
from Auth.models import AuthUser
from Auth.decorators import org_user_login_required

import re
import hashlib
import datetime

# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate password
        if not phone.isdigit() or len(phone) != 10:
            messages.warning(request, 'Enter a valid Phone Number.')          
        if password != confirm_password:
            messages.warning(request, 'Password should be same as confirm password.')
        if len(password) < 8:
            messages.warning(request, 'Password should be at least 8 characters long.')
        if not re.search("[a-z]", password):
            messages.warning(request, 'Password should have at least one lowercase letter.')
        if not re.search("[A-Z]", password):
            messages.warning(request, 'Password should have at least one uppercase letter.')
        if not re.search("[0-9]", password):
            messages.warning(request, 'Password should have at least one numeric character.')
        if not re.search("[!@#$%^&*]", password):
            messages.warning(request, 'Password should have at least one special character (!@#$%^&*).')

            return render(request, 'Auth/RegisterView.html')

        combined = password + phone
        hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
        current_time = datetime.datetime.now().timestamp()

        # Check if phone already exists
        if AuthUser.objects.filter(phone=phone).exists():
                messages.warning(request, 'Phone exists')
                return render(request, 'Auth/RegisterView.html')
        # What if phone already does not exists
        else:
            print(combined)
            print(hash)
            custom_user = AuthUser.objects.create(full_name=full_name, phone=phone, password=hash)
            custom_user.save()

            if AuthUser.objects.filter(phone=phone).exists():
                User = AuthUser.objects.get(phone=phone)

                session_id = str(User.uuid) + str(current_time)

                User.session_id = session_id
                User.save()

                request.session['org_user_id'] = session_id

                return redirect('DashView')
            return redirect('LoginView')
    response = render(request, 'Auth/RegisterView.html')
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

def LoginView(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Check if the user exists in the database
        try:
            if not phone.isdigit() or len(phone) != 10:
                messages.warning(request, 'Enter a valid Phone Number.')
                return redirect('LoginView')            
            User = AuthUser.objects.get(phone=phone)

            # Check if the password matches the hash in the database
            combined = password + phone
            hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
            if User.password != hash:
                messages.warning(request, 'Incorrect password.')
                return redirect('LoginView')

            # Create a session ID and store it in the user's record and in the session
            current_time = datetime.datetime.now().timestamp()
            session_id = str(User.uuid) + str(current_time)
            User.session_id = session_id
            User.save()
            request.session['org_user_id'] = session_id

            return redirect('DashView')

        except AuthUser.DoesNotExist:
            messages.warning(request, 'User not found.')
            return redirect('LoginView')

    response = render(request, 'Auth/LoginView.html')
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

def LogoutView(request):
    if 'org_user_id' in request.session:
        del request.session['org_user_id']

    # Redirect the user to the login page
    return redirect('LoginView')

@org_user_login_required
def UsersView(request):
    Users = AuthUser.objects.all()[:100]
    # set up search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            Users = AuthUser.objects.filter(full_name__icontains=keyword)
    data = {
        'Users': Users,
    }
    return render(request, 'Auth/UsersView.html', data)

@org_user_login_required
def UserAddView(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Validate password
        if not phone.isdigit() or len(phone) != 10:
            messages.warning(request, 'Enter a valid Phone Number.')          
        if password != confirm_password:
            messages.warning(request, 'Password should be same as confirm password.')
        if len(password) < 8:
            messages.warning(request, 'Password should be at least 8 characters long.')
        if not re.search("[a-z]", password):
            messages.warning(request, 'Password should have at least one lowercase letter.')
        if not re.search("[A-Z]", password):
            messages.warning(request, 'Password should have at least one uppercase letter.')
        if not re.search("[0-9]", password):
            messages.warning(request, 'Password should have at least one numeric character.')
        if not re.search("[!@#$%^&*]", password):
            messages.warning(request, 'Password should have at least one special character (!@#$%^&*).')

            return redirect('UsersView')

        # Check if phone already exists
        if AuthUser.objects.filter(phone=phone).exists():
                messages.warning(request, 'Phone exists')
                return redirect('UsersView')
        # What if phone already does not exists
        else:
            if password == confirm_password:
                combined = password + phone
                hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
                create_user = AuthUser.objects.create(full_name=full_name, phone=phone, password=hash)
                create_user.save()
                messages.success(request, 'User Added Successfully')

    response = redirect('UsersView')
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

@org_user_login_required
def UserUpdateView(request):
    if request.method == 'POST':
        uuid = request.POST.get('uuid')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        # Validate password
        if not phone.isdigit() or len(phone) != 10:
            messages.warning(request, 'Enter a valid Phone Number.')
        if password:
            if password != confirm_password:
                messages.warning(request, 'Password should be same as confirm password.')
            if len(password) < 8:
                messages.warning(request, 'Password should be at least 8 characters long.')
            if not re.search("[a-z]", password):
                messages.warning(request, 'Password should have at least one lowercase letter.')
            if not re.search("[A-Z]", password):
                messages.warning(request, 'Password should have at least one uppercase letter.')
            if not re.search("[0-9]", password):
                messages.warning(request, 'Password should have at least one numeric character.')
            if not re.search("[!@#$%^&*]", password):
                messages.warning(request, 'Password should have at least one special character (!@#$%^&*).')

                return redirect('UsersView')


        if password:
            if password == confirm_password:
                combined = password + phone
                hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
                update_user = AuthUser.objects.get(pk=uuid)
                update_user.full_name = full_name
                update_user.phone = phone
                update_user.password = hash
                update_user.save()
                messages.success(request, 'User Updated Successfully')
        if not password:
            update_user = AuthUser.objects.get(pk=uuid)
            update_user.full_name = full_name
            update_user.phone = phone
            update_user.save()
            messages.success(request, 'User Updated Successfully')

    response = redirect('UsersView')
    response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response

@org_user_login_required
def UserDeleteView(request):
    if request.method == 'POST':
        uuid = request.POST.get('uuid')
        print(uuid)
        delete_user = AuthUser.objects.get(pk=uuid)
        delete_user.delete()
        messages.info(request, 'User Permanently Deleted')
    return redirect('UsersView')