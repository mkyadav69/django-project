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

class AboutPageView(TemplateView):
    template_name = 'admin/partials/about.html'

class WorkPageView(TemplateView):
    template_name = 'admin/partials/work.html'

class EducationPageView(TemplateView):
    template_name = 'admin/partials/education.html'

class ExperiencePageView(TemplateView):
    template_name = 'admin/partials/experience.html'

class SkillPageView(TemplateView):
    template_name = 'admin/partials/skill.html'

class BlogPageView(TemplateView):
    template_name = 'admin/partials/blog.html'

class ProjectPageView(TemplateView):
    template_name = 'admin/partials/project.html'

class SongPageView(TemplateView):
    template_name = 'admin/partials/song.html'

class VideoPageView(TemplateView):
    template_name = 'admin/partials/video.html'

class PersonalInfoPageView(TemplateView):
    template_name = 'admin/partials/personal_info.html'