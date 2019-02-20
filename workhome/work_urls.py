from django.urls import path
from . import work_views
urlpatterns = [
    path('hello/<name>/<int:age>',work_views.hello),
    path('page/',work_views.page),
    path('page/hahahaha',work_views.page2,name='new_page'),
    path('index/',work_views.index)
]