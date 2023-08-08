from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path("", views.main),
    path('logout/', views.logout_view, name='logout'),
    path("profile", views.profile, name="profile"),
    path("home", views.main, name="home")
    # Add logout and profile URL patterns as needed
]