from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, DetailView
from .models import Company, Statement 

class IndexView(TemplateView):
  template_name = 'chart/index.html'

  def get_context_data(self, **kwargs):
    statement_list = Statement.objects.all().order_by('company')
    params = {'statement_list': statement_list,}
    return params

class CompanyView(DetailView):
  model = Company

  def get_context_data(self, **kwargs):
    company_name = kwargs['object'].name
    statement_list = Statement.objects.filter(company=kwargs['object']).order_by('-fiscal_year')[:4]
    params = {
        'company_name': company_name,
        'statement_list': statement_list,
    }
    return params

class StatementView(DetailView):
  model = Statement