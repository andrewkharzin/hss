import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from django.http import FileResponse
from django.shortcuts import render
from .models import AogService
from apps.agents.models import Agent
from apps.services.models import DutyPerson
from apps.stuffs.models import Aog

from django.views.generic import ListView
from .tables import AogRequestTable
from django_filters.views import FilterView
from django_tables2 import SingleTableView


def index(request):
    return render(request, 'index.html')


def aog_srv_pdf_report(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    # Add some lines of text
    lines = [
        "Line 1",
        "Line 2",
        "Line 3"
    ]

    # Loop
    for line in lines:
        textob.textLine(line)
    # Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='Aog_request_order_report.pdf')


@login_required(login_url="accounts:login")
def aog_aservices_request(request):

    aogs = AogService.objects.all()
    agents = Agent.objects.all()
    persons = DutyPerson.objects.all()
    flight_kits = Aog.objects.all()

    total_request = aogs.count()

    # delivered = orders.filter(status='Delivered').count()
    # pending = orders.filter(status='Pending').count()

    context = {
        "total_request": total_request,
        "aogs": aogs,
        "agents": agents,
        "persons": persons,
        "flight_kits": flight_kits,
         
    }
    # 'total_orders':total_orders,'delivered':delivered,
    # 'pending':pending }

    return render(request, "aogservices.html", context)


class AogRequestListView(SingleTableView, FilterView):
    model = AogService
    table_class = AogRequestTable
    template_name = 'aogservices.html'

    