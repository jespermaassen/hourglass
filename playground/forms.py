from django.forms import ModelForm
from timedcontracts.models import Contract

class ContactForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['size', 'status']
