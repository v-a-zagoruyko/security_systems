from django.db import models
from django.utils.translation import ugettext_lazy as _

class Sellout(models.Model):
  image = models.ImageField(_('Изображение'), upload_to='sellout')

  class Meta:
    verbose_name = _('Акция')
    verbose_name_plural = _('Акции')

class Cert(models.Model):
  image = models.ImageField(_('Изображение'), upload_to='cert')

  class Meta:
    verbose_name = _('Сертификат')
    verbose_name_plural = _('Сертификаты')

class Partners(models.Model):
  title = models.CharField(_('Название'), max_length=128)
  description = models.TextField(_('Описание'), max_length=1024)
  image = models.ImageField(_('Изображение'), upload_to='partners')
  link = models.URLField(_('Ссылка'), max_length=256, blank=True,)

  class Meta:
    verbose_name = _('Партнер')
    verbose_name_plural = _('Партнеры')

class Delivery(models.Model):
  title = models.CharField(_('Название'), max_length=128)
  description = models.TextField(_('Описание'), max_length=1024)
  image = models.ImageField(_('Изображение'), upload_to='partners')
  link = models.URLField(_('Ссылка'), max_length=256, blank=True,)

  class Meta:
    verbose_name = _('Служба доставки')
    verbose_name_plural = _('Службы доставки')

class ItemCategory(models.Model):
  title = models.CharField(_('Название'), max_length=128)
  nested = models.ManyToManyField(
    "self",
    symmetrical=False,
    blank=True,
    related_name='nestedCategory',
    verbose_name='Подкатегории'
    )

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = _('Категорию оборудования')
    verbose_name_plural = _('Категории оборудования')

class Item(models.Model):
  kind = models.ForeignKey(
    ItemCategory,
    on_delete=models.CASCADE,
    related_name='category',
    verbose_name='Категория оборудования'
  )
  title = models.CharField(_('Название'), max_length=256)
  description = models.TextField(_('Описание'), max_length=1024)
  size = models.CharField(_('Размер'), max_length=256)
  cost = models.PositiveSmallIntegerField(_('Цена'), )
  cost_sale = models.PositiveSmallIntegerField(
    _('Цена cо скидкой'),
    default=0,
    help_text='Если больше нуля, товар отображается в категории распродажа'
  )
  image = models.ImageField(_('Изображение'), upload_to='item')

  def __str__(self):
    return self.title

  def get_sale(self):
    if self.cost_sale:
      return self.cost - self.cost_sale
    else:
      return False

  class Meta:
    verbose_name = _('Оборудование')
    verbose_name_plural = _('Оборудование')