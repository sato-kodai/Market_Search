from django.contrib import admin

# Register your models here.
from .models import Company, Statement

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  list_display = ('name',)
  list_display_links = ('name',)


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
  list_display = ('company', 'fiscal_year')
  list_display_links = ('company',)
