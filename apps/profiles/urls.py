from django.urls import path, re_path
from .views import ProfileDetailView

app_name = "profiles"


urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view(), name="detail"),
    # path('<int:pk>/update', ProfileUpdateView.as_view(), name="profile_update")
]
