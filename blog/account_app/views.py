from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from account_app.forms import ArticleCreationForm
from main_app.models import Tag, Article


class AuthorArticlesListView(LoginRequiredMixin, ListView):
    """Список статей пользователя"""
    template_name = 'account_app/my_articles.html'

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('draft')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Написание новой статьи"""
    template_name = 'account_app/new_article.html'
    form_class = ArticleCreationForm

    def post(self, request, *args, **kwargs):
        form = ArticleCreationForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            tags = form.cleaned_data['tags']
            article.save()
            if len(tags):
                for item in tags:
                    tag = Tag.objects.get(pk=item.pk)
                    article.tags.add(tag)
            return redirect(reverse('account_app:my_articles'))
        return redirect(reverse('account_app:new_article'))


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'account_app/edit_article.html'
    success_url = reverse_lazy('account_app:my_articles')

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs['pk'])
        if request.user != article.author:
            return redirect(reverse('main_app:index'))
        return super().get(request, *args, **kwargs)
