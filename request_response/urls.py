from django.urls import path
from . import views
urlpatterns=[
    path('post_test/',views.post_test),
    path('get_test/',views.get_test),
    path('upload/',views.upload_file),
    path('response_test/',views.response_test),
    path('response_test2/',views.response_test2),
    path('set_cookie/',views.set_cookie),
    path('get_cookie/',views.get_cookie),
    path('delete_cookie/',views.delete_cookie),
]