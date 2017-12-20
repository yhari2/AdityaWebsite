from django.shortcuts import render
from django.views.generic.base import View
from database.models import Post

class HomePage(View):
    def get(self, request):
        postsList = Post.objects.all()[::-1]
        context = {}
        context["posts"] = postsList
        return render(request, 'index.html', context)

