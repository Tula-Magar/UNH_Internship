"""internship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from internships import views
from django.contrib.auth.decorators import login_required

APP_NAME = "internship"

urlpatterns = [
    path('registration/login/', LoginView.as_view(), name="login"),
    path('registration/register/', views.register, name="register"),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('upload/', views.upload_spreadsheet, name='upload'),
    path('acounts/', include("django.contrib.auth.urls")),
    path('students/', views.display_students, name='students'),
    path('internships/', views.display_internships, name='internships'),
    path('internship_assignments/', views.display_internship_assignments,
         name='internship_assignments')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
