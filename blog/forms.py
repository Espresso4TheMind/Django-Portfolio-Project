from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name'
        }))

    body = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Leave a comment!',
            }))
