# # myProfile/urls.py
# from django.urls import path

# from .views import homePageView

# urlpatterns = [
#     path('', homePageView, name='home')
# ]


# myProfile/urls.py
from django.urls import path
from .views.admin_views import AdminPageView,AboutPageView,WorkPageView,EducationPageView,ExperiencePageView,SkillPageView,BlogPageView,ProjectPageView,VideoPageView,SongPageView,PersonalInfoPageView

urlpatterns = [
    path('', AdminPageView.as_view(), name='adminManoj'),
    path('about', AboutPageView.as_view(), name='about'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('education', EducationPageView.as_view(), name='education'),
    path('experience', ExperiencePageView.as_view(), name='experience'),
    path('personalInfo', PersonalInfoPageView.as_view(), name='personalInfo'),
    path('skill', SkillPageView.as_view(), name='skill'),
    path('song', SongPageView.as_view(), name='song'),
    path('video', VideoPageView.as_view(), name='video'),
    path('work', WorkPageView.as_view(), name='work'),
    path('project', ProjectPageView.as_view(), name='project'),   
]
