from django import forms
from django.contrib.auth.models import User
from myapp.models import *




class Loginform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control','placeholder':'user name'}),
            "password":forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        }


class Examform(forms.ModelForm):
    class Meta:
        model=Exmreg
        fields="__all__"
        # fields=["Nameofthe_department"]
        widgets={
            "student_name":forms.TextInput(attrs={'class':'form-control','placeholder':'student_name'}),
            "Address":forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            "Nameofthe_department":forms.Select(attrs={'class':'form-control','placeholder':'Nameofthe_department'}),
            "Nameofthe_course":forms.Select(attrs={'class':'form-control','placeholder':'Nameofthe_course'}),
            "enrollment":forms.NumberInput(attrs={'class':'form-control','placeholder':'enrollment'}),
        }

    # def __init__(self, *args, **kwargs):
    #         name_of_the_department = Department.objects.all().order_by('department_name').values_list('department_name')
    #         self.fields['Nameofthe_department'] = forms.CharField(label="Department", required=True,
    #                                                  widget=forms.Select(choices=name_of_the_department,
    #                                                       attrs={'style': 'width: 300px;'}))
        # self.fields['form_name'] = forms.CharField(label="Form/Class Name", required=False, initial="", max_length=50)


from django import forms
from .models import Courses

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['department', 'course_name', 'available_seats']
        widgets = {
            'department': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%;',
            }),
            'course_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course name',
            }),
            'available_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter available seats',
                'min': '0',
            }),
        }
        labels = {
            'department': 'Department',
            'course_name': 'Course Name',
            'available_seats': 'Available Seats',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select Department"

        
        

class DepartmentAddform(forms.ModelForm):
    class Meta:
        model=Department
        fields=['department_name','description','image']

    
class Userregform(forms.ModelForm):
    class Meta:
        model=User
        fields= fields = ["first_name","last_name","email","username","password"]
        widgets = {
                    'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
                    'username':forms.TextInput(attrs={'class':'form-control'}),
                    'password':forms.PasswordInput(attrs={'class':'form-control'})
        }





