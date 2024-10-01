from Auth.models import AuthUser


def User(request):
    User = None
    if 'org_user_id' in request.session:
        session_id = request.session['org_user_id']
        User = AuthUser.objects.get(session_id=session_id)
    data = {
        'User': User
    }
    return (data)
