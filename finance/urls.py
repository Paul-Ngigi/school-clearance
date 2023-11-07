from django.urls import path
from .views import DetailsView, ClearanceList, clearanceDetails, initiateReview, reviewClearance

urlpatterns = [        
    path('details', DetailsView.as_view(), name='finance_details_view'),
    path('list', ClearanceList.as_view(), name='finance_clearance_list_view'),
    path('clearance-details/<pk>', clearanceDetails, name='finance_clearance_details_view'),    
    path('review/<pk>', initiateReview, name='finance_initiate_view'),
    path('review-clearance', reviewClearance, name='finance_review_clearance_view'),
]
