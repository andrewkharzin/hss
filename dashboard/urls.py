from django.urls import path
from apps.orders.views import order_analytics
from apps.services.views import aog_aservices_request, AogRequestListView
from dashboard.views import dashboard

app_name = "dashboard"

urlpatterns = [
    path('dahsboarf/', dashboard, name="board" ),
    path('dashboard/order/states', order_analytics, name="order_states"),
    path('dashboard/oags/states/request', AogRequestListView.as_view(), name="aogs_list_request"),
]
