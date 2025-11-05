from django.shortcuts import render,redirect
from .models import Conference,Submission
from django.views.generic import ListView , DetailView , CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ConferenceForm , SubmissionForm
from django.contrib.auth.mixins import LoginRequiredMixin 

def liste_conferences(request):
    conferences = Conference.objects.all()
    return render(request, "conferences/liste.html", {"liste": conferences})

def details_index(request):
    return redirect("liste_conferences")

class ConferenceList(ListView):
    model = Conference
    context_object_name = "liste"
    template_name = "conferences/liste.html"

class ConferenceDetails(DetailView):
    model = Conference
    template_name = "conferences/details.html"
    context_object_name = "conference"

class ConferenceCreate(LoginRequiredMixin , CreateView):
    model = Conference
    template_name = "conferences/form.html"
    #fields = ["name", "theme", "location", "description", "start_date", "end_date"]
    form_class=ConferenceForm
    success_url = reverse_lazy("liste_conferences")

class ConferenceUpdate(LoginRequiredMixin , UpdateView):
    model = Conference
    template_name = "conferences/form.html"
    #fields = ["name", "theme", "location", "description", "start_date", "end_date"]
    form_class=ConferenceForm
    success_url = reverse_lazy("liste_conferences")

class ConferenceDelete(LoginRequiredMixin , DeleteView):
    model = Conference
    template_name = "conferences/delete.html"
    success_url = reverse_lazy("liste_conferences")

class SubmissionList(ListView):
    model = Submission
    context_object_name = "liste"
    template_name = "submissions/liste.html"


class SubmissionDetailView(DetailView):
    model = Submission
    template_name = "submissions/details.html" 
    context_object_name = "submission"

class SubmissionCreate(LoginRequiredMixin , CreateView):
    model = Submission
    template_name = "submissions/form.html"
    form_class=SubmissionForm
    success_url = reverse_lazy("submission_list")


class SubmissionUpdate(UpdateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'submissions/modifier.html'




    