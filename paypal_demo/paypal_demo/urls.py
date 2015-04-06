from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
  url(r'^$', 'paypal_demo.views.home', name='home'),
  
  url(r'^paypal-ipn/', include('paypal.standard.ipn.urls')),
  
  url(r'^admin/', include(admin.site.urls)),
]
