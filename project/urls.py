#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/',include('FallInApp.urls'))
]
