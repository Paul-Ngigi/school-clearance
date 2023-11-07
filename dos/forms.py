from django import forms
from clearance.models import Review


class ReviewForm(forms.ModelForm):           
    class Meta:
        model = Review
        fields = ['approved', 'rejected', 'reason']        