from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from .models import Journal, Principle, Idea, Decision, Aphorism
# Create your views here.


class JournalCreate(CreateView):
    model = Journal
    fields = '__all__'
    success_url = reverse_lazy('journals')#reverse_lazy('Journal')


class JournalUpdate(UpdateView):
    model = Journal
    fields = '__all__'


class JournalDelete(DeleteView):
    model = Journal
    success_url = reverse_lazy('index')



class JournalView(generic.ListView):
    model = Journal
    template_name = 'compendium_app/journal.html'
    queryset = Journal.objects.filter(data_type='Real')


class PrincipleView(generic.ListView):
    model = Principle
    template_name = 'compendium_app/principle.html'
    queryset = Principle.objects.filter(journal_id__data_type='Real')



class IdeaView(generic.ListView):
    model = Idea
    template_name = 'compendium_app/idea.html'
    queryset = Idea.objects.filter(journal_id__data_type='Real')



class DecisionView(generic.ListView):
    model = Decision
    template_name = 'compendium_app/decision.html'
    queryset = Decision.objects.filter(journal_id__data_type='Real')


class AphorismView(generic.ListView):
    model = Aphorism
    template_name = 'compendium_app/aphorism.html'
    queryset = Aphorism.objects.filter(journal_id__data_type='Real')

