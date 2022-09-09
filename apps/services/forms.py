from django import forms
from apps.stuffs.models import Aog

from apps.services.models import AogService


class ServiceRequestItemListForm(forms.ModelForm):
    # here we only need to define the field we want to be editable
    fields = ['service_item',]
    service_item = forms.ModelMultipleChoiceField(
        queryset=Aog.objects.all(), required=False)