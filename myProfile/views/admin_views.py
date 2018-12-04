from django.shortcuts import render

# Create your views here.
# myProfile/views.py
from django.http import HttpResponse

from django.views.generic import TemplateView

# def homePageView(request):
#     return HttpResponse('Hello, World!')

    # myProfiles/views.py


class AdminPageView(TemplateView):
    template_name = 'admin.html'