from django.urls import path
from .views import DetailsView, ClearanceList, clearanceDetails, initiateReview, reviewClearance

urlpatterns = [        
    path('details', DetailsView.as_view(), name='sae_details_view'),
    path('list', ClearanceList.as_view(), name='sae_clearance_list_view'),
    path('clearance-details/<pk>', clearanceDetails, name='sae_clearance_details_view'),    
    path('review/<pk>', initiateReview, name='sae_initiate_view'),
    path('review-clearance', reviewClearance, name='sae_review_clearance_view'),
]
