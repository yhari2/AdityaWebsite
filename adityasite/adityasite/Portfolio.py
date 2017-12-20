from django.shortcuts import render
from django.views.generic.base import View

class Portfolio(View):
    def get(self, request):
        return render(request, 'Portfolio.html')