from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 
from reviews import views  # This is where you import your views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reviews.urls')),  # API URLs handled by reviews app
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),  # signup using views from the reviews app
    path('', views.index, name='index'),  # Add a root path URL
]

