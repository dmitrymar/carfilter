from django.contrib import admin
from .models import Post, Carmodel

admin.site.register(Post)
class CarmodelAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model', 'version', 'body', 'drive')
admin.site.register(Carmodel, CarmodelAdmin)
