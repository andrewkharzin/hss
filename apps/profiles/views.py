from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from .forms import ProfileForm, form_validation_error # import the used form and related function to show errors
from .models import Profile 
from apps.organizations.models import Organization

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.utils import timezone


# @method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile/profile_detail'