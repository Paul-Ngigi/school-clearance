from django.urls import path
from .views import DetailsView, ClearanceList, ClearanceDetails, ReviewClearance

urlpatterns = [
    path('details', DetailsView.as_view(), name='hostels_details_view'),
    path('list', ClearanceList.as_view(), name='hostels_clearance_list_view'),
    path('clearance-details/<pk>', ClearanceDetails.as_view(),
         name='hostels_clearance_details_view'),
    path('review/<pk>', ReviewClearance.as_view(),
         name='hostels_review_view'),
]
