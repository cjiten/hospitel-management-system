from django.urls import path
from Auth import views

urlpatterns = [
    path('login/', views.LoginView, name='LoginView'),
    path('register/', views.RegisterView, name="RegisterView"),
    path('logout/', views.LogoutView, name="LogoutView"),
    
    path('user/', views.UsersView, name="UsersView"),
    path('user/add/', views.UserAddView, name="UserAddView"),
    path('user/update/', views.UserUpdateView, name="UserUpdateView"),
    path('user/delete/', views.UserDeleteView, name="UserDeleteView"),
]
