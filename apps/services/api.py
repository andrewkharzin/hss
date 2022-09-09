from ninja import NinjaAPI
from apps.services.models import AogService
from apps.services.schema import AogServiceSchema
from typing import List

api = NinjaAPI()


@api.get('/apps/services/aogs/list', response=List[AogServiceSchema])
def get_list_request_aog_services(request):
    return AogService.objects.all()
