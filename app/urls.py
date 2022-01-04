#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from FallInApp import views



# add url patterns to match each Model-- object
urlpatterns = [
    url(r'^user',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi)
    #url(r'^org-user$',view.org_userApi)
    #url(r'^org-user/([0-9]+)$',view.org_userApi)
]
