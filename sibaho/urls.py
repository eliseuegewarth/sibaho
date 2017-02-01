from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^sibaho/', include(admin.site.urls)),
    url(r'^', include('empregado.urls')),
]
