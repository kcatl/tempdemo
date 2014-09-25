from django.conf.urls import patterns, include, url
from weiboheat import views
from kcatl import settings
from weiboheat import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', views.index),
    url(r'getData$', views.getData),
    url(r'test$', views.test),
    url(r'login$', views.login), 
    
    
)