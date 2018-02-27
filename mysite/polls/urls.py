from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
