from django.contrib import admin
from .models import Mineral

class MineralAdmin(admin.ModelAdmin):
    model = Mineral

admin.site.register(Mineral, MineralAdmin)
