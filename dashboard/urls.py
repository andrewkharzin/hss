from django.urls import path
from apps.orders.views import order_analytics
from apps.services.views import aog_aservices_request, AogRequestListView
from dashboard.views import dashboard

app_name = "dashboard"

urlpatterns = [
    #User Profile ProfileView
    #path('dashboard/user/', ProfileView.as_view(), name="user_profile"),
    # path('dashboard/profile/settings/<int:pk>/', ProfileUpdateView.as_view(), name="profile_settings"),
    path('', dashboard, name="board" ),
    path('dashboard/order/states', order_analytics, name="order_states"),
    path('dashboard/oags/states/request', AogRequestListView.as_view(), name="aogs_list_request"),
]
