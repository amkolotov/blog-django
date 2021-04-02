from django import forms

from main_app.models import Article


class ArticleCreationForm(forms.ModelForm):
    """"Форма написания новой статьи"""

    class Meta:
        model = Article
        fields = ('title', 'category', 'tags', 'poster', 'short_desc', 'text', 'draft')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
