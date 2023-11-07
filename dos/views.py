from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View
from clearance.models import Clearance, Review
from .forms import ReviewForm

# Create your views here.             
class DetailsView(View):
    template_name = 'dos/details.html'
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
    template_name = 'dos/clearance-list.html'
    title = 'Details'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):                      
        user = request.user       
        clearances = Clearance.objects.all()            
        context = {
            'title': self.title,            
            'user': user,
            'clearances': clearances
        }    
        return render(request, self.template_name, context)   
    
def clearanceDetails(request, pk):                              
    clearance = Clearance.objects.get(id=pk)   
    reviews = Review.objects.filter(id=pk)  
    hasBeenReviewed = False
    if len(reviews) > 0:
        for review in reviews:            
            if review.reviewer.role == 'DEAN_OF_STUDENTS':
                hasBeenReviewed = True                                    
            if review.reviewer.role != '':
                hasBeenReviewed = False
    context = {        
        'clearance': clearance,
        'reviews': reviews,
        'hasBeenReviewed': hasBeenReviewed
    }
    return render(request, 'dos/clearance-details.html', context)


def initiateReview(request, pk):
    form = ReviewForm()      
    template_name = 'dos/review.html'
    title = 'Review'
        
    form = ReviewForm(request.POST or None)    
    current_url = request.path
    clearanceId = current_url.split('/')[-1]
    print(clearanceId)
    context = {
        'title': title,                        
        'form': form
    }    
    return render(request, template_name, context)       

def reviewClearance(request):
    form = ReviewForm(request.POST or None)      
    template_name = 'dos/review.html'
    title = 'Review'
    print('clicked')
        
    if form.is_valid():
        print('valid')
    context = {
        'title': title,                        
        'form': form
    }    
    return render(request, template_name, context)  

        