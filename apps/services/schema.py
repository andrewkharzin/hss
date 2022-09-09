from ninja import ModelSchema
from apps.services.models import AogService


class AogServiceSchema(ModelSchema):
    class Config:
        model = AogService
        model_fields = "__all__"
