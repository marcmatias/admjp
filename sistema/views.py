from django.shortcuts import render
from django.views import generic

class IndexListView(generic.TemplateView):
	template_name = 'sistema/index.html'