# # myProfile/urls.py
# from django.urls import path

# from .views import homePageView

# urlpatterns = [
#     path('', homePageView, name='home')
# ]


# myProfile/urls.py
from django.urls import path

from .views.web_views import HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]