from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog

from locking.views import lock, unlock, is_locked, js_variables

urlpatterns = [
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/lock/$', lock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/unlock/$', unlock),
    url(r'(?P<app>[\w-]+)/(?P<model>[\w-]+)/(?P<id>\d+)/is_locked/$', is_locked),
    url(r'variables\.js$', js_variables, name='locking_variables'),
]

urlpatterns += [
    url(r'jsi18n/$', JavaScriptCatalog.as_view(packages=['locking'])),
]
