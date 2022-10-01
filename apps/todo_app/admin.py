from django.contrib import admin
from apps.todo_app.models import ToDoItem, ToDoList, Category
from mptt.admin import DraggableMPTTAdmin

class CategoryAdmin(DraggableMPTTAdmin):
    pass

admin.site.register(ToDoItem)
admin.site.register(ToDoList)
admin.site.register(Category, DraggableMPTTAdmin)