from django.contrib import admin
from .models import Result, Question
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Result)
class userdetails(ImportExportModelAdmin):
    pass

admin.site.register(Question)
