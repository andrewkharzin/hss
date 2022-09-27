import django_tables2 as tables
from .models import AogService
from django.utils.html import format_html
from apps.agents.models import Agent
from django.utils.html import escape
from django.utils.safestring import mark_safe


class ImageColumn(tables.Column):
    model = Agent
    def render(self, value):
        return mark_safe('<img src="uploads/agents/icons/%Y/%m/%d/%s.png" />'
                % escape(value))
        
        
TEMPLATE = '''
   <a class="text-dark fw-bolder text-hover-primary fs-6">{{ flight_ac_reg }}</a>
   <span class="text-muted fw-bold text-muted d-block fs-7"><a></a>Moo</span>
'''


class ImageColumn(tables.Column):
    def render(self, value):
        return mark_safe('<img src="{url}" />' % escape(value))

class AogRequestTable(tables.Table):
    image = ImageColumn('icon')
    agent = tables.TemplateColumn(TEMPLATE)
    service_name = tables.Column(attrs={"td": {"class": "text-dark fw-bolder text-hover-primary fs-6"}})
    flight = tables.Column(attrs={"td": {"class": "text-dark fw-bolder text-hover-primary fs-6"}})
    flight_ac_reg = tables.Column(attrs={"tf": {"class":"badge badge-light-success"}})
    flight_date = tables.Column(attrs={"td": {"class": "text-dark fw-bolder text-hover-primary fs-6"}})
    
    
    class Meta:
        model = AogService
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("",)