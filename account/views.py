from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, UserForm
from django.contrib import messages
from utils.views import send_mails
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
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
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')            
            form.save()
            student = User.objects.get(email=email) 
            print(student.role)           
            student.role = 'STUDENT'
            student.save()
            print(student.role)           
            send_mails(
                request,
                'mailing/welcome.html',
                'Welcome to school clearance',              
                [email],
                {'first_name': first_name}
            )
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
                        cod = CHAIRMAN_OF_DEPARTMENT.find_cod_by_email(email)
                        if cod is not None:
                            login(request, user)
                            return redirect('cod_details_view')
                        else:
                            CHAIRMAN_OF_DEPARTMENT.objects.create(user=user)
                            login(request, user)
                            return redirect('cod_details_view')
                    elif user_roles == 'LIBRARY':
                        library = LIBRARY.find_library_by_email(email)
                        if library is not None:
                            login(request, user)
                            return redirect('library_details_view')
                        else:
                            LIBRARY.objects.create(user=user)
                            login(request, user)
                            return redirect('library_details_view')
                    elif user_roles == 'SPORTS_AND_ENTERTAINMENT':
                        sae = SPORTS_AND_ENTERTAINMENT.find_sae_by_email(email)
                        if sae is not None:
                            login(request, user)
                            return redirect('sae_details_view')
                        else:
                            SPORTS_AND_ENTERTAINMENT.objects.create(user=user)
                            login(request, user)
                            return redirect('sae_details_view')
                    elif user_roles == 'HOSTELS':
                        hostel = HOSTEL.find_hostel_by_email(email)
                        if hostel is not None:
                            login(request, user)
                            return redirect('hostels_details_view')
                        else:
                            HOSTEL.objects.create(user=user)
                            login(request, user)
                            return redirect('hostel_details_view')
                    elif user_roles == 'FINANCE':
                        finance = FINANCE.find_finance_by_email(email)
                        if finance is not None:
                            login(request, user)
                            return redirect('finance_details_view')
                        else:
                            FINANCE.objects.create(user=user)
                            login(request, user)
                            return redirect('finance_details_view')
                    elif user_roles == 'DEAN_OF_STUDENTS':
                        dos = CHAIRMAN_OF_DEPARTMENT.find_cod_by_email(email)
                        if dos is not None:
                            login(request, user)
                            return redirect('dos_details_view')
                        else:
                            login(request, user)
                            return redirect('dos_details_view')
                    elif user_roles == 'REGISTRAR':
                        registrar = REGISTRAR.find_registrar_by_email(email)
                        if registrar is not None:
                            login(request, user)
                            return redirect('registrar_details_view')
                        else:
                            REGISTRAR.objects.create(user=user)
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
                    messages.warning(request, "User cannot be found")
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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home_view')