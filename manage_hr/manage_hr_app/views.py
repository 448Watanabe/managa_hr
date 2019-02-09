# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Student
from django.db.models import Q

# Create your views here.

class IndexView(generic.ListView):
    model = Student
    paginate_by = 10

    """
    def get_queryset(self):
        queryset = Student.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset
    """