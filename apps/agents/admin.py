from django.contrib import admin
from apps.agents.models import Agent

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = [
        'agent_id',
        'thumbnail_preview',
       
]