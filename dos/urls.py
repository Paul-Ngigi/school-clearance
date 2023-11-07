from django.urls import path
from .views import DetailsView, ClearanceList, clearanceDetails, initiateReview, reviewClearance

urlpatterns = [        
    path('details', DetailsView.as_view(), name='dos_details_view'),        
    path('list', ClearanceList.as_view(), name='dos_clearance_list_view'),
    path('clearance-details/<pk>', clearanceDetails, name='dos_clearance_details_view'),    
    path('review/<pk>', initiateReview, name='dos_initiate_view'),
    path('review-clearance', reviewClearance, name='dos_review_clearance_view'),
]
