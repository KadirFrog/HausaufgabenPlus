from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path("", views.main),
    path('logout/', views.logout_view, name='logout'),
    path("profile", views.profile, name="profile"),
    path("home", views.main, name="home"),
    path('create/', views.create_post, name='create'),
    # Add logout and profile URL patterns as needed
]

handler404 = 'haplus.views.custom_404'
