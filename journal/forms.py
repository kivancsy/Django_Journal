from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entry Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Start writing your journal entry here...', 'rows': 10}),
        }