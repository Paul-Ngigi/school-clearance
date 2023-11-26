from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from clearance.models import Clearance, Review
from .forms import ReviewForm
from utils.views import send_mails

# Create your views here.
class DetailsView(View):
    template_name = 'cod/details.html'
    title = 'Details'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        context = {
            'title': self.title,
            'user': user
        }
        return render(request, self.template_name, context)


class ClearanceList(View):
    template_name = 'cod/clearance-list.html'
    title = 'Details'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        user = request.user
        clearances = Clearance.objects.all().order_by('-initiated_at')
        context = {
            'title': self.title,
            'user': user,
            'clearances': clearances
        }
        return render(request, self.template_name, context)


class ClearanceDetails(View):
    def get(self, request, pk, *args, **kwargs):
        clearance = Clearance.objects.get(id=pk)
        reviews = Review.objects.filter(clearance=pk).order_by('-created_at')
        hasBeenReviewed = False
        if len(reviews) > 0:
            for review in reviews:
                if review.reviewer.role == 'cod':
                    hasBeenReviewed = True
        context = {
            'clearance': clearance,
            'reviews': reviews,
            'hasBeenReviewed': hasBeenReviewed
        }
        return render(request, 'cod/clearance-details.html', context)


class ReviewClearance(View):
    template_name = 'cod/review.html'
    title = 'Review'

    def get(self, request, pk, *args, **kwargs):
        form = ReviewForm()
        current_url = request.path
        clearanceId = current_url.split('/')[-1]
        print(clearanceId)
        context = {
            "form": form,
            "clearanceId": clearanceId
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        form = ReviewForm(request.POST or None)
        clearance = None
        user = None
        try:
            clearance = Clearance.objects.get(id=pk)
        except Clearance.DoesNotExist:
            return HttpResponse("Clearance not found", status=404)

        user = request.user
        if form.is_valid() and clearance is not None and user is not None:
            approved = form.cleaned_data.get('approved')
            reason = form.cleaned_data.get('reason')
            review = Review.objects.create(
                clearance=clearance, reviewer=user, approved=approved, reason=reason)            
            clearance = Clearance.objects.get(id=pk)
            clearance.status = "Chairman Of Departments Reviewed"            
            clearance.save()    
            student = clearance.student
            student_name = student.user.first_name
            send_mails(
                request,
                'mailing/clearance-reviewed.html',
                'Clearance Reviewed by Chairman of Department',
                [student.user.email],
                {'user': user, 'clearance': clearance,
                    'review': review, 'student_name': student_name}
            )                 
            return redirect('cod_clearance_details_view', pk)
        context = {
            'title': self.title,
            'form': form
        }
        return render(request, self.template_name, context)
