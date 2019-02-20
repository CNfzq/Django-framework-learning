from django.urls import path
from . import views_5
urlpatterns = [
    # path('add/',views_5.add_user),
    # path('search/',views_5.search_user),
    # path('delete/',views_5.delete_user),
    # path('update/',views_5.update_user),
    path('add_ftest/',views_5.add_ftest)
]