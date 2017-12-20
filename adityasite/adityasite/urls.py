"""adityasite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from adityasite.views import HomePage
from adityasite.AboutMePage import AboutMePage
from adityasite.Portfolio import Portfolio

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view()),   # '^$' means start and end without seeing anything
    url(r'AboutMePage', AboutMePage.as_view()), # handles the about me page
    url(r'Portfolio', Portfolio.as_view()), # handles Portfolio page
]
