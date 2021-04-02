from django.urls import path

from .views import ArticleListView, IndexView, TagArticleListView, ArticleDetailView

app_name = 'main_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:pk>/', ArticleListView.as_view(), name='articles'),
    path('category/<int:pk>/page/<int:page>/', ArticleListView.as_view(), name='page'),
    path('tag/<int:pk>/', TagArticleListView.as_view(), name='tag_articles'),
    path('tag/<int:pk>/page/<int:page>/', TagArticleListView.as_view(), name='page_tag'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
]
