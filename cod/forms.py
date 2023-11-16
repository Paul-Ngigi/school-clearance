from django import forms
from clearance.models import Clearance, Review


class ReviewForm(forms.ModelForm):           
    class Meta:
        model = Review
        fields = ['approved', 'reason']        