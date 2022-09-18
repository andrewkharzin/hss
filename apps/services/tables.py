import django_tables2 as tables
from .models import AogService
from django.utils.html import format_html
from apps.agents.models import Agent
from django.utils.html import escape
from django.utils.safestring import mark_safe


class ImageColumn(tables.Column):
    model = Agent
    def render(self, value):
        return mark_safe('<img src="{{agent.icon}}" />'
                % escape(value))

class AogRequestTable(tables.Table):
    image  = ImageColumn('icon')
    class Meta:
        model = AogService
        template_name = "django_tables2/bootstrap.html"
        fields = ("image", "agent", "service_name", "flight", "flight_ac_reg", "flight_date", "fix_required", "responsibles_persons", )