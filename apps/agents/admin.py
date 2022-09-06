from django.contrib import admin
from apps.agents.models import Agent


# class AgentAdmin(admin.ModelAdmin):
#     list_display = [
#         'agent_id',
#         'agent_company',
#         'phone_number',
    # ]

admin.site.register(Agent)
