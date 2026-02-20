from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from journal.models import JournalEntry
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import JournalEntryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def home(request):
    recent_entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')[:3] if request.user.is_authenticated else []
    context = {
        'recent_entries': recent_entries
    }
    return render(request, 'journal/home.html', context)


@login_required
def entry_list(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')  # ← filter(user=request.user) eklendi
    context = {
        'entries': entries
    }
    return render(request, 'journal/entry_list.html', context)


@login_required
def EntryDetail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)  # ← user=request.user eklendi
    context = {
        'entry': entry
    }
    return render(request, 'journal/entry_detail.html', context)


class EntryCreate(LoginRequiredMixin, CreateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = 'journal/entry_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('journal:entry_detail', kwargs={'pk': self.object.pk})

    
class EntryUpdate(LoginRequiredMixin, UpdateView):
    model = JournalEntry
    form_class = JournalEntryForm
    template_name = 'journal/entry_update.html'
    
    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)
    
    def get_success_url(self):
        return reverse('journal:entry_detail', kwargs={'pk': self.object.pk})

    
class EntryDelete(LoginRequiredMixin, DeleteView):
    model = JournalEntry
    success_url = reverse_lazy('journal:entry_list')
    
    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)