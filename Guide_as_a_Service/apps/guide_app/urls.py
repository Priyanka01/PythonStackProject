from django.conf.urls import url
from . import views           
# from ..login_app import views

urlpatterns = [
    url(r'^$', views.guide_profile_page),
    url(r'^$', views.update_profile_page_display),
    
]