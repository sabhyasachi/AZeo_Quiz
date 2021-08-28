from django.contrib import admin
from .models import Result
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Result)
class userdetails(ImportExportModelAdmin):
    pass