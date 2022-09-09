from typing import List
from apps.profiles.models import Profile
from ninja import NinjaAPI
from apps.profiles.schema import UserProfileSchema


api = NinjaAPI()


@api.get("/profiles", response=List[UserProfileSchema])
def category_list(request):
    qs = Profile.objects.all()
    return qs
