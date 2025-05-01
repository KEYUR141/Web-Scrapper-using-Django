from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('imdb_scrap',imdb_index,name="IMDBHome"),
    path('imdb_run_scrapper/',imdb_run_scrapper),
    path('toi_run_scrapper/',toi_run_scrapper),
    path('toi_scrap',toi_index,name="TOIHome"),
    path('celery/',main_index),
    path('',Main_Page)

]