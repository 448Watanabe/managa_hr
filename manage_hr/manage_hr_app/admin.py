# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student, Friend, BelongSchool, DesiredSchool

admin.site.register(Student)
admin.site.register(Friend)
admin.site.register(BelongSchool)
admin.site.register(DesiredSchool)