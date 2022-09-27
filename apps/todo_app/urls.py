from django.urls import path

from . import views
from .views import ListListView, ItemListView

app_name = "qnote"

urlpatterns = [
    path("qnotes/", ListListView.as_view(), name="index"),
    path("qnotes/list/<int:list_id>/", ItemListView.as_view(), name="list"),
    path("qnotes/list/add/", views.ListCreate.as_view(), name="list-add"),
    path("qnotes/list/<int:list_id>/item/add/", views.ItemCreate.as_view(), name="item-add",),
    path("qnotes/list/<int:list_id>/item/<int:pk>/", views.ItemUpdate.as_view(), name="item-update",),
    path("qnotes/list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    path("qnotes/list/<int:list_id>/item/<int:pk>/delete/", views.ItemDelete.as_view(), name="item-delete", ),
]
