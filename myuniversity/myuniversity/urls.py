"""
URL configuration for myuniversity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name='home'),
    # path('course',views.Home2.as_view(),name='course'),
    path('list',views.COURSE.as_view(),name='list'),
    path('login',views.Login.as_view(),name='login'),
    path('logout',views.Logout.as_view(),name='logout'),
    path('reg',views.Register.as_view(),name='reg'),
    path('course',views.CourseaddView.as_view(),name='addcourse'),
    path('dept',views.DepartmentAddView.as_view(),name='departadd'),
    path('signup',views.SignupView.as_view(),name='signup'),
    path('listreg',views.Listreg.as_view(),name='listreg'),
    path('Edit/<int:id>',views.Editform.as_view(),name='Edit'),
    path('Delete/<int:id>',views.Deleteform.as_view(),name='Delete'),
    path('admin',views.AdminIndex.as_view(),name='admin')




    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

