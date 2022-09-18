from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.orders.models import Order
from apps.services.models import AogService
from apps.agents.models import Agent


@login_required(login_url="accounts:login")
def order_analytics(request):
    orders = Order.objects.filter()
    aogs = AogService.objects.all()
    agents = Agent.objects.all()

    total_orders = orders.count()

    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()

    context = {
        "orders": orders,
        "total_orders": total_orders,
        "aogs": aogs,
        "agents": agents,

    }
    # 'total_orders':total_orders,'delivered':delivered,
    # 'pending':pending }

    return render(request, "analytics/orders.html", context)
