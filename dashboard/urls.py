from django.urls import path
from apps.orders.views import order_analytics
from dashboard.views import dashboard

app_name = "dashboard"

urlpatterns = [
    path('dahsboarf/', dashboard, name="board" ),
    path('dashboard/order/states', order_analytics, name="order_states"),
]
