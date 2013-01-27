import models
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
  list_display = ('title',)

class HomePicAdmin(admin.ModelAdmin):
  list_display = ('position',)

class SupplierAdmin(admin.ModelAdmin):
  list_display = ('name',)

class PortfolioPhotoAdmin(admin.ModelAdmin):
  list_display = ('title',)

admin.site.register(models.Page, PageAdmin)
admin.site.register(models.HomePic, HomePicAdmin)
admin.site.register(models.Supplier, SupplierAdmin)
admin.site.register(models.PortfolioPhoto, PortfolioPhotoAdmin)
