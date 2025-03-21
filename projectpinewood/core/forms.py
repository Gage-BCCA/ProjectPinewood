from django import forms
from core.models import Subscriber, InterestTag


class SubscriptionForm(forms.ModelForm): #Unsure how to apply interests here, remind me to ask questions about it.
    class Meta:
        model = Subscriber
        fields = ['email', 'first_name', 'interests']
    
    def valid_email(self):
        email = self.cleaned_data['email']
        if Subscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email