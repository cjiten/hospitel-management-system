# from django.shortcuts import redirect
# from django.urls import reverse

# class AuthCheckMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if not 'org_user_id' in request.session:
#             return redirect(reverse('login'))
#         return self.get_response(request)
    
#     # settings.py

# MIDDLEWARE = [
#     # Other middleware classes...
#     'yourapp.middleware.AuthCheckMiddleware',
# ]
