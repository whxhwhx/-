from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^login_handle/', views.login_handle),
    url(r'user_list/(\d+)/', views.user_list),
    url(r'visitor_list/(\d+)/', views.visitor_list),
    url(r'dangerous_list/(\d+)', views.dangerous_list),
    url(r'logout', views.logout),
    url(r'detail/(\d+)/', views.detail),
    url(r'upload_img', views.upload_img),
    url(r'console/', views.console_index),
    url(r'^about/', views.about),
    url(r'^contact/', views.contact),
]
