from django.utils import timezone
from django.conf import settings
from pytils.translit import slugify
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.urls import reverse

class Category(MPTTModel):
  name = models.CharField(max_length=55, unique=True)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
  slug = models.SlugField(max_length=55, null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  
  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    verbose_name_plural = 'Categories'
    
  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    value = self.name
    if not self.slug:
      self.slug = slugify(self.name)
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('qnote:category-list/', args=[str(self.slug)])


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = TreeForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(
      max_length=55,
    )

    def get_absolute_url(self):
        kwargs = {
        'slug': self.slug
        }
        return reverse("qnote:list", args=[self.id])

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
      if not self.slug:
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
      super().save(*args, **kwargs)

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    

    class Meta:
        ordering = ["due_date"]
        