from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.contrib.filters.admin import RangeDateFilter

from .models import Report


@admin.register(Report)
class ReportAdmin(ModelAdmin):
    list_display = ["title", "filter_date", "editable_date"]
    list_editable = ["editable_date"]
    list_filter = [("filter_date", RangeDateFilter)]
    search_fields = ["title"]
    list_filter_submit = False
