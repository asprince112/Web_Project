from django.views.generic import TemplateView

# Create your views here.

class PostListView(TemplateView):
    template_name = 'blog_list.html'