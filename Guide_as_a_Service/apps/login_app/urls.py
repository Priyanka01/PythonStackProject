from django.conf.urls import url
from . import views    
# from guide_app.views import guide_app 
# from ..guide_app import views      

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^sucess$',views.sucess),
    url(r'^login_app/signup$',views.signup_window),
    url(r'^login_app/register$',views.register),
    url(r'^login_app/login$', views.login),

    # url(r'^guide_app$',guide_app)
]
