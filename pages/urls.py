from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('listings/insta/', views.qwerty, name='insta'),
    path('admin/', admin.site.urls),
]
