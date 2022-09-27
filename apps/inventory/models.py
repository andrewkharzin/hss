from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from apps.users.models import User


class Category(MPTTModel):
  name = models.CharField(max_length=50, unique=True)
  parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
  slug = models.SlugField()

  class MPTTMeta:
    order_insertion_by = ['name']

  class Meta:
    unique_together = (('parent', 'slug',))
    verbose_name_plural = 'categories'

  def get_slug_list(self):
    try:
      ancestors = self.get_ancestors(include_self=True)
    except:
      ancestors = []
    else:
      ancestors = [ i.slug for i in ancestors]
    slugs = []
    for i in range(len(ancestors)):
      slugs.append('/'.join(ancestors[:i+1]))
    return slugs

  def __str__(self):
    return self.name

class BaseInventory(models.Model):
     inv_name = models.CharField(_("Inventory Name"), max_length=50)
     category = TreeForeignKey(Category, null=True,blank=True)
     created_at = models.DateTimeField(auto_now_add=True)
     update_at = models.DateTimeField(auto_now=True)
     
     class Meta:
         abstract = True
         
class Inventory(BaseInventory):
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)