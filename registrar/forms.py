from django import forms
from clearance.models import Clearance, Review


class ReviewForm(forms.ModelForm):           
    # bools = [('Yes','Yes'),('No','No')]
    # approved = forms.CharField(label='Approve', widget=forms.RadioSelect(choices=bools))
    # rejected = forms.CharField(label='Reject', widget=forms.RadioSelect(choices=bools))
    class Meta:
        model = Review
        fields = ['approved', 'reason']        
            