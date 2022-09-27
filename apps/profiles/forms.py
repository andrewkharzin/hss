from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    position = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=13)
    full_name = forms.CharField(max_length=255)

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    """
    Form Validation Error
    If any error happened in your form, this function returns the error message.
    """
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg