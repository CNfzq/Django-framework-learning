from django.urls import path
from . import views_3
urlpatterns = [
    path('03_index_01/',views_3.index_03_01),
    path('03_index_02/',views_3.index_03_02),
    path('03_index_03/',views_3.static_files)
]