from django.urls import path
from .views import DetailsView, ClearanceList, ClearanceDetails, ReviewClearance

urlpatterns = [
    path('details', DetailsView.as_view(), name='dos_details_view'),
    path('list', ClearanceList.as_view(), name='dos_clearance_list_view'),
    path('clearance-details/<pk>', ClearanceDetails.as_view(),
         name='dos_clearance_details_view'),
    path('review/<pk>', ReviewClearance.as_view(),
         name='dos_review_view'),
]
