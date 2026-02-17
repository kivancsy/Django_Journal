from django.shortcuts import render
from django.http import HttpResponse
from journal.models import JournalEntry
# Create your views here.

def Home(request):
    return render(request, 'journal/home.html')

def EntryList(request):
    entries = JournalEntry.objects.all()
    context = {
        'entries': entries
    }
    return render(request, 'journal/entry_list.html', context)