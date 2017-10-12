# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ToDoWork , DoingWork


admin.site.register(ToDoWork)
admin.site.register(DoingWork)
