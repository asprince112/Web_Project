from django.views.generic import TemplateView

# Create your views here.

class FansHome(TemplateView):
    template_name = 'fans_index.html'

class MillerHome(TemplateView):
    template_name = 'miller.html'

class OscarHome(TemplateView):
    template_name = 'oscar.html'

class SamHome(TemplateView):
    template_name = 'sam.html'

class WilliamHome(TemplateView):
    template_name = 'william.html'

class KobeHome(TemplateView):
    template_name = 'kobe.html'

class TimHome(TemplateView):
    template_name = 'tim.html'