from Auth.models import AuthUser
from django.shortcuts import redirect

def org_user_login_required(function):
    def wrapper(request, login_url='LoginView', *args, **kwargs):
        if 'org_user_id' in request.session:
            session_id = request.session['org_user_id']
            if AuthUser.objects.filter(session_id=session_id).exists():
                return function(request, *args, **kwargs)
        return redirect(login_url)
    return wrapper