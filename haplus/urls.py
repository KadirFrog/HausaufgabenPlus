from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.main, name='home'),  # Change the name to 'home'
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create_post, name='create'),
    path('lehrerinfo/', views.lehrerinfo, name='lehrerinfo'),
    path("accounts/login/", views.login_view),
    path('control_panel/', views.control_panel, name='control_panel'),
    # Add logout and profile URL patterns as needed
]

handler404 = 'haplus.views.custom_404'
