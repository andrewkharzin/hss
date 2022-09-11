from django.urls import path
from apps.services import views
from apps.services.views import index

app_name = 'services'

urlpatterns = [
    path('aog_srv_pdf_report', views.aog_srv_pdf_report, name='aog_srv_pdf_report'),
    path('services/', index, name='index')
]
