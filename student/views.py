from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import StudentSignUpForm
from django.contrib import messages
from .models import Student
from clearance.models import Clearance, Review
from utils.views import send_mails

# Create your views here.


class ProfileView(View):
    template_name = 'students/profile.html'
    user_form = StudentSignUpForm
    title = 'Profile'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.user_form(request.POST or None)
        context = {
            'form': form,
            'title': self.title
        }
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.user_form(request.POST or None)
        authenticated_user = request.user
        if form.is_valid():
            form.instance.user = authenticated_user
            form.save()
            messages.success(request, 'Registered Successfully')
            return redirect('student_details_view')
        form = self.user_form(request.POST or None)
        context = {'form': form}
        return render(request, self.template_name, context)


class DetailsView(View):
    template_name = 'students/details.html'
    title = 'Details'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        student = Student.find_student_by_email(user.email)
        clearances = len(Clearance.objects.filter(student=student))
        context = {
            'title': self.title,
            'student': student,
            'user': user,
            'clearances': clearances
        }
        return render(request, self.template_name, context)


class InitiateClearance(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        email = user.email        
        student = Student.find_student_by_email(email)
        clearance = Clearance.objects.create(student=student)
        send_mails(
            request,
            'mailing/clearance-initiated.html',
            'Clearance Initiated',
            [email],
            {'user': user, 'clearance': clearance}
        )
        if clearance:
            return redirect('student_list_clearance_view')
        else:
            messages.error('Something went wrong')
            return render(request, 'students/details.html')


class ClearanceListView(View):
    template_name = 'students/clearance-list.html'
    title = 'Clearance List'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        student = Student.find_student_by_email(user.email)
        clearances = Clearance.objects.filter(
            student=student).order_by('-initiated_at')
        context = {
            'title': self.title,
            'clearances': clearances
        }
        return render(request, self.template_name, context)


def clearanceDetails(request, pk):
    user = request.user
    student = Student.find_student_by_email(user.email)
    clearance = Clearance.objects.get(id=pk)
    reviews = Review.objects.filter(clearance_id=pk).order_by('-created_at')
    print(len(reviews))
    context = {
        'student': student,
        'clearance': clearance,
        'reviews': reviews
    }
    return render(request, 'students/clearance-details.html', context)


def reviewDetails(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review': review
    }
    return render(request, 'students/review-details.html', context)
