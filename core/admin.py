from django.contrib import admin
from .models import Unit, Result
# Register your models here.
admin.site.register(Unit)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ["student", "unit", "cat", "exam", "total"]