# # myProfile/urls.py
# from django.urls import path

# from .views import homePageView

# urlpatterns = [
#     path('', homePageView, name='home')
# ]


# myProfile/urls.py
from django.urls import path
from .views.admin_views import AdminPageView
urlpatterns = [
    path('', AdminPageView.as_view(), name='adminManoj'),
]