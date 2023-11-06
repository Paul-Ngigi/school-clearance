from django.urls import path
from .views import DetailsView, ClearanceList, clearanceDetails, initiateReview, reviewClearance

urlpatterns = [        
    path('details', DetailsView.as_view(), name='registrar_details_view'),
    path('list', ClearanceList.as_view(), name='registrar_clearance_list_view'),
    path('clearance-details/<pk>', clearanceDetails, name='clearance_clearance_details_view'),    
    path('review/<pk>', initiateReview, name='initiate_view'),
    path('review-clearance', reviewClearance, name='review_clearance_view'),
]
