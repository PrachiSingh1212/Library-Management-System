from django.contrib import admin
from .models import *

# Register your models here
from django.contrib import admin
from .models import reader

@admin.register(reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('reference_id', 'reader_name')
