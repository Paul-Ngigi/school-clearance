from django.urls import path
from .views import DetailsView

urlpatterns = [        
    path('details', DetailsView.as_view(), name='library_details_view'),        
]
