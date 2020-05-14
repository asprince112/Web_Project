from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.models import Article
from blog.forms import ArticleForm
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.

class ArticleList(ListView):
    model = Article

    def get_queryset(self):
        return Article.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class ArticleDetail(DetailView):
    model = Article


class CreateArticleView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/article_detail.html'
    #login_required 是 decorator, 它只能用在 function view,
    #而 class view 要用 LoginRequiredMixin, 所以要加入上面兩行
    form_class = ArticleForm
    model = Article


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/article_list.html'
    form_class = ArticleForm
    model = Article


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:article_list')

@login_required
def article_publish(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('blog:article_detail', pk=pk)