from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy
from django.http import Http404
from .models import Journal, Principle, Idea, Decision, Aphorism


# Create your views here.


class JournalCreate(CreateView):
    model = Journal
    fields = '__all__'
    success_url = reverse_lazy('journals')


class JournalUpdate(UpdateView):
    model = Journal
    fields = '__all__'
    success_url = reverse_lazy('journals')


class JournalDelete(DeleteView):
    model = Journal
    success_url = reverse_lazy('index')


class JournalDetailView(generic.DetailView):
    model = Journal


class JournalView(generic.ListView):
    model = Journal
    template_name = 'compendium_app/journal.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user, data_type='Real')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        else:
            return super(JournalView, self).get(self, request, *args, **kwargs)


class PrincipleView(generic.ListView):
    model = Principle
    template_name = 'compendium_app/principle.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user, journal_id__data_type='Real')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        else:
            return super(PrincipleView, self).get(self, request, *args, **kwargs)


class IdeaView(generic.ListView):
    model = Idea
    template_name = 'compendium_app/idea.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user, journal_id__data_type='Real')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        else:
            return super(IdeaView, self).get(self, request, *args, **kwargs)


class DecisionView(generic.ListView):
    model = Decision
    template_name = 'compendium_app/decision.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user, journal_id__data_type='Real')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        else:
            return super(DecisionView, self).get(self, request, *args, **kwargs)


class AphorismView(generic.ListView):
    model = Aphorism
    template_name = 'compendium_app/aphorism.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user, journal_id__data_type='Real')

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        else:
            return super(AphorismView, self).get(self, request, *args, **kwargs)


