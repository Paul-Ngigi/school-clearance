from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, UserForm
from django.contrib import messages
# Models
from student.models import Student
from cod.models import CHAIRMAN_OF_DEPARTMENT
from dos.models import DEAN_OF_STUDENTS
from finance.models import FINANCE
from hostels.models import HOSTEL
from library.models import LIBRARY
from registrar.models import REGISTRAR
from sae.models import SPORTS_AND_ENTERTAINMENT

User = get_user_model()


# Create your views here.
class SignUpView(View):
    """
    Sign up view
    """
    title = 'signup'    
    template_name = 'accounts/signup.html'
    def get(self, request, *args, **kwargs):
        form = UserForm
        context = {"title": self.title, "form": form}
        if request.user.is_authenticated:
            return redirect('home_view')
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)                  
        if form.is_valid():            
            form.save()            
            return redirect('login_view')                    

        return render(request, 'accounts/signup.html', {"form": form})


class SignInView(View):
    """
    Sign in view
    """
    form = LoginForm()
    template_name = 'accounts/signin.html'

    def get(self, request, *args, **kwargs):        
        if request.user.is_authenticated:            
            return redirect('home_view')
        return render(request, self.template_name)   

    def post(self, request, *args, **kwargs):        
        form = LoginForm(request.POST or None)        
        if form.is_valid():                        
            email = form.cleaned_data.get("email")            
            password = form.cleaned_data.get("password")                        
            if email and password:                    
                user = authenticate(request, username=email, password=password)                                                                                                        
                if user is not None:                                       
                    user_roles = user.role                    
                    if user_roles == 'CHAIRMAN_OF_DEPARTMENT':                                                      
                        if not CHAIRMAN_OF_DEPARTMENT.objects.filter(user=user).exists():
                           CHAIRMAN_OF_DEPARTMENT.objects.create(user=user)
                           login(request, user)
                           return redirect('cod_details_view')
                        else:
                            login(request, user)
                            return redirect('cod_details_view')
                    elif user_roles == 'LIBRARY':                                                      
                        if not LIBRARY.objects.filter(user=user).exists():
                           LIBRARY.objects.create(user=user)
                           login(request, user)
                           return redirect('library_details_view')
                        else:
                            login(request, user)
                            return redirect('library_details_view') 
                    elif user_roles == 'SPORTS_AND_ENTERTAINMENT':                                                      
                        if not SPORTS_AND_ENTERTAINMENT.objects.filter(user=user).exists():
                           SPORTS_AND_ENTERTAINMENT.objects.create(user=user)
                           login(request, user)
                           return redirect('sae_details_view')
                        else:
                            login(request, user)
                            return redirect('sae_details_view')
                    elif user_roles == 'HOSTELS':                                                      
                        if not HOSTEL.objects.filter(user=user).exists():
                           HOSTEL.objects.create(user=user)
                           login(request, user)
                           return redirect('hostel_details_view')
                        else:
                            login(request, user)
                            return redirect('hostel_details_view')
                    elif user_roles == 'FINANCE':                                                      
                        if not FINANCE.objects.filter(user=user).exists():
                           FINANCE.objects.create(user=user)
                           login(request, user)
                           return redirect('finance_details_view')
                        else:
                            login(request, user)
                            return redirect('finance_details_view')
                    elif user_roles == 'DEAN_OF_STUDENTS':                                                      
                        if not DEAN_OF_STUDENTS.objects.filter(user=user).exists():
                           DEAN_OF_STUDENTS.objects.create(user=user)
                           login(request, user)
                           return redirect('dos_details_view')
                        else:
                            login(request, user)
                            return redirect('dos_details_view')
                    elif user_roles == 'REGISTRAR':                                                      
                        if not REGISTRAR.objects.filter(user=user).exists():
                           REGISTRAR.objects.create(user=user)
                           login(request, user)
                           return redirect('registrar_details_view')
                        else:
                            login(request, user)
                            return redirect('registrar_details_view')                                        
                    elif user_roles == 'STUDENT':                                                      
                        student = Student.find_student_by_email(email) 
                        if student is not None:  
                            login(request, user)                                              
                            return redirect('student_details_view')
                        else:
                            login(request, user)
                            return redirect('student_profile_view')  
                    else:
                        messages.success(request, "Login as admin")                                                                                                                                                                     
                else:
                    messages.warning(request,"User cannot be found")
                    request.session['invalid_user'] = 1
        else:
            messages.error("")
            print("Error")
        context = {"form": form}
        return render(request, self.template_name, context)


class SignOutView(View):
    """
    Sign out view
    """

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login_view')