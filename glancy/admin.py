import models
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
  list_display = ('title',)

class HomePicAdmin(admin.ModelAdmin):
  list_display = ('position',)

admin.site.register(models.Page, PageAdmin)
admin.site.register(models.HomePic, HomePicAdmin)
