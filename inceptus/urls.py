from django.urls import path

from . import views

app_name = 'inceptus'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('query', views.query, name='query'),
    path('results', views.results, name='results'),
]
