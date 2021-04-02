from django.urls import path

from .views import ArticleCreateView, AuthorArticlesListView, ArticleUpdateView

app_name = 'account_app'

urlpatterns = [
    path('new-article/', ArticleCreateView.as_view(), name='new_article'),
    path('edit-article/<int:pk>', ArticleUpdateView.as_view(), name='edit_article'),
    path('', AuthorArticlesListView.as_view(), name='my_articles'),
]
