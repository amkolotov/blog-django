from django import forms

from main_app.models import Reviews


class ReviewForm(forms.ModelForm):
    """Форма написания отзыва к товару"""

    class Meta:
        model = Reviews
        fields = ('text',)

        widgets = {'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'comment', 'rows': 3})}
