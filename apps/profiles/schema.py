from ninja import ModelSchema
from .models import Profile


class UserProfileSchema(ModelSchema):
    class Config:
        model = Profile
        model_fields = [
            'user',
            'agent'
        ]