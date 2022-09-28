from pyexpat import model
import django_tables2 as tables
from .models import Agent
from django.utils.html import format_html
from django.utils.html import escape
from django.utils.safestring import mark_safe




class ImageColumn(tables.Column):
    model = Agent
    def render(self, value):
        return mark_safe('<img src="/media/uploads/agents/icons/2022/09/18/nw.png" />'
                % escape(value))
