from django.conf.urls import url
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^ajax/admin/', include('locking.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('staticfiles.urls')),
]
