from django.urls import path
from .views import ProfileView, DetailsView, InitiateClearance, ClearanceListView, clearanceDetails

urlpatterns = [    
    path('profile', ProfileView.as_view(), name='student_profile_view'),        
    path('details', DetailsView.as_view(), name='student_details_view'),        
    path('initiate-clearance', InitiateClearance.as_view(), name='student_initiate_clearance_view'),        
    path('clearance-list', ClearanceListView.as_view(), name='student_list_clearance_view'),
    path('clearance-details/<pk>', clearanceDetails, name='student_clearance_details_view'),
]
