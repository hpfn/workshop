
from django.urls import path

from workshop.core import views as core_views

app_name = 'core'

urlpatterns = [
    path('', core_views.index, name='index'),
    path('success/', core_views.success, name='success'),

]