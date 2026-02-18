from django.shortcuts import render
from django.http import HttpResponse
from journal.models import JournalEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import JournalEntryForm



def Home(request):
    recent_entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')[:3] if request.user.is_authenticated else []
    context = {
        'recent_entries': recent_entries
    }
    return render(request, 'journal/home.html', context)

def EntryList(request):
    entries = JournalEntry.objects.all().order_by('-created_at')
    context = {
        'entries': entries
    }
    return render(request, 'journal/entry_list.html', context)

def EntryDetail(request, pk):
    entry = JournalEntry.objects.get(pk=pk)
    context = {
        'entry': entry
    }
    return render(request, 'journal/entry_detail.html', context)

class EntryCreate(CreateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = 'journal/entry_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('journal:entry_detail', kwargs={'pk': self.object.pk})
    
class EntryUpdate(UpdateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = 'journal/entry_update.html'
    
    def get_success_url(self):
        return reverse('journal:entry_detail', kwargs={'pk': self.object.pk})
    
class EntryDelete(DeleteView):
    model = JournalEntry
    success_url = reverse_lazy('journal:entry_list')
    
    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)