from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import View

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