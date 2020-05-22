from django.contrib import admin
from django.utils.html import format_html

from .models import *

admin.site.site_url = 'https://xn-----8kcdhncqegn1asmcnzbjcin9q.xn--p1ai'
admin.site.site_header = 'ГК Системы Безопасности'

@admin.register(Sellout)
class SelloutAdmin(admin.ModelAdmin):
  def image_tag(self, obj):
    return format_html('<img style="width: 125px" src="{}" />'.format(obj.image.url))

  image_tag.short_description = 'Изображение'
  list_display = ('id', 'image_tag')

@admin.register(Cert)
class CertAdmin(admin.ModelAdmin):
  def image_tag(self, obj):
    return format_html('<img style="width: 125px" src="{}" />'.format(obj.image.url))

  image_tag.short_description = 'Изображение'
  list_display = ('id', 'image_tag')

@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
  def image_tag(self, obj):
    return format_html('<img style="width: 125px" src="{}" />'.format(obj.image.url))

  image_tag.short_description = 'Изображение'
  list_display = ('id', 'image_tag', 'title', 'link')

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
  def image_tag(self, obj):
    return format_html('<img style="width: 125px" src="{}" />'.format(obj.image.url))

  image_tag.short_description = 'Изображение'
  list_display = ('id', 'image_tag', 'title', 'link')

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'title')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
  def image_tag(self, obj):
    return format_html('<img style="width: 125px" src="{}" />'.format(obj.image.url))

  image_tag.short_description = 'Изображение'
  list_display = ('id', 'image_tag', 'title', 'size', 'cost', 'cost_sale',)
  search_fields = ('title',)