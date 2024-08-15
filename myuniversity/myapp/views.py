from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from django.core.mail import send_mail, settings
from myapp.models import Courses,Exmreg,Department
from django.views import View
from myapp.forms import Loginform,Examform,CourseForm,DepartmentAddform,Userregform
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    template_name='index.html'
    model=Department
    context_object_name='dep'




class COURSE(ListView):
    model = Courses
    template_name = 'course.html'
    context_object_name = "data"
   
class Login(View):
    def get(self,request):
        form=Loginform
        return render(request,'login.html',{"form":form})
    def post(self,request):
        username=(request.POST.get("username"))
        password=(request.POST.get("password"))
        user=authenticate(request,username=username,password=password)
        if user:
            if user.is_staff:
               login(request,user)
               return redirect('admin')
            else:
                login(request,user)
                return redirect('reg')
        else:
            
            return redirect('home')
        

class Logout(View):

    def get(self,request):
        logout(request)
        return redirect('login')

    
class Register(CreateView):
    form_class = Examform
    template_name = 'reg.html'
    model = Exmreg
    success_url=reverse_lazy('listreg')

class CourseaddView(CreateView):
    template_name='course-add.html'
    form_class=CourseForm
    model=Courses
    success_url=reverse_lazy('list')

class DepartmentAddView(CreateView):
    template_name='department-add.html'
    form_class=DepartmentAddform
    model=Department
    success_url=reverse_lazy('home')


   
class SignupView(CreateView):
    model=User
    form_class=Userregform
    template_name='signup.html'
    success_url=reverse_lazy('login')

    def form_valid(self, form):
        User.objects.create_user(**form.cleaned_data)
        return redirect('login')
    

class Listreg(ListView):
    model = Exmreg
    template_name = 'reg_list.html'
    context_object_name = "datakey"



class Editform(UpdateView):
    model = Exmreg
    form_class = Userregform
    template_name = 'form_edit.html'
    success_url = reverse_lazy('listreg')
    pk_url_kwarg = 'id'

class Deleteform(DeleteView):
    model = Exmreg
    template_name = 'form_delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listreg')

class AdminIndex(ListView):
    template_name='admin-index.html'
    model=Department
    context_object_name='dep'
