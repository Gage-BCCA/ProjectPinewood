from django import forms
from core.models import Subscriber, InterestTag


class SubscriptionForm(forms.ModelForm): 
    class Meta:
        model = Subscriber
        fields = ['email', 'first_name', 'wants_newsletter', 'wants_product_updates']
    
    def valid_email(self):
        email = self.cleaned_data.get('email')
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email