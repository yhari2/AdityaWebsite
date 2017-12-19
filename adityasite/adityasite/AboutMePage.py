from django.shortcuts import render
from django.views.generic.base import View

class AboutMePage(View):
    def get(self, request):
        return render(request, 'AboutMePage.html')