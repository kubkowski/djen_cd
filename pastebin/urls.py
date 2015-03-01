from django.conf.urls import patterns, url
from django.views.generic import View

from models import Paste

urlpatterns = patterns('',
    url(r'$', CreateView, { 'model': Paste}),
)