from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View
from clearance.models import Clearance, Review
from .forms import ReviewForm

# Create your views here.
class DetailsView(View):
    template_name = 'sae/details.html'
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
    template_name = 'sae/clearance-list.html'
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
                if review.reviewer.role == 'sae':
                    hasBeenReviewed = True
        context = {
            'clearance': clearance,
            'reviews': reviews,
            'hasBeenReviewed': hasBeenReviewed
        }
        return render(request, 'sae/clearance-details.html', context)


class ReviewClearance(View):
    template_name = 'sae/review.html'
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
            clearance.status = "Sports & Entertainment Reviewed"            
            clearance.save()                     
            return redirect('sae_clearance_details_view', pk)
        context = {
            'title': self.title,
            'form': form
        }
        return render(request, self.template_name, context)
