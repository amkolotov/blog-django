from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import View

from .models import Article, Category, Tag


class IndexView(View):
    """Главная страница"""
    def get(self, request):
        return HttpResponseRedirect(reverse('main_app:articles', args=(0,)))


class ArticleListView(ListView):
    """Вывод списка статей категории"""
    paginate_by = 4

    def get_queryset(self):
        if self.kwargs['pk'] == 0:
            article = Article.objects.filter(draft=False, news=False).first()
            print(article.tags.all())
            return Article.objects.filter(draft=False, news=False)
        return Article.objects.filter(category__pk=self.kwargs['pk'], draft=False, news=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['pk'] == 0:
            category = {'pk': 0, 'name': 'Все'}
        else:
            category = get_object_or_404(Category, pk=self.kwargs['pk'], draft=False)
        context.update({'category': category})
        return context


class TagArticleListView(ListView):
    """Вывод списка статей по тегу"""
    paginate_by = 2

    def get_queryset(self):
        return Article.objects.filter(tags__pk=self.kwargs['pk'], draft=False, news=False)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        context.update({'tag': tag})
        return context


class ArticleDetailView(DetailView):
    """Просмотр статьи"""
    model = Article


class SearchView(View):
    """Обработка поискового запроса"""

    def get(self, request):
        search = request.GET.get('search')
        if search:
            category = Category.objects.filter(name__icontains=search, draft=False)
            if category:
                return redirect(reverse('main_app:articles', args=[category.first().pk]))
            tag = Tag.objects.filter(name__icontains=search)
            if tag:
                return redirect(reverse('main_app:tag_articles', args=[tag.first().pk]))
            article = Article.objects.filter(title__icontains=search, draft=False)
            if article:
                return redirect(reverse('main_app:article', args=[article.first().pk]))

        return redirect(reverse('main_app:index'))
