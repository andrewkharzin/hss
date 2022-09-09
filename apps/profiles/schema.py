from ninja import ModelSchema
from .models import Profile


class UserProfileSchema(ModelSchema):
    class Config:
        model = Profile
        model_fields = [
            'user',
            'first_name',
            'last_name',
            'phone_number',
            'phone_number_mobile',
            'email',
            'position',
            'user_image',
]