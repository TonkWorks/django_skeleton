from django.views import generic
from django.shortcuts import get_object_or_404, render

from django.utils import timezone
from jobs.models import Job
from jobs.models import Event


class Analytic(generic.TemplateView):
    template_name = "home.html"


    def get_context_data(self, **kwargs):
            context = super(HomePage, self).get_context_data(**kwargs)
            context.update(
                {
                    'jobs': Job.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3],
                    'events': Event.objects.filter(date__gte=timezone.now()).order_by('date')[:3]
                })
            return context


class JobsPage(generic.TemplateView):
    template_name = "jobs.html"

    def get_context_data(self, **kwargs):
            context = super(JobsPage, self).get_context_data(**kwargs)
            context.update(
                {
                    'results': Job.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:100]
                })
            return context


class JobsDetailPage(generic.TemplateView):
    def get(self, request, pk):
        p = get_object_or_404(Job, pk=pk)
        return render(request, 'jobs-detail.html', {
            'job': p,
        })

class EventsPage(generic.TemplateView):
    template_name = "events.html"

    def get_context_data(self, **kwargs):
            context = super(EventsPage, self).get_context_data(**kwargs)
            context.update(
                {
                    'results': Event.objects.filter(date__gte=timezone.now()).order_by('date')[:100]
                })
            return context


class EventsDetailPage(generic.TemplateView):
    def get(self, request, pk):
        p = get_object_or_404(Event, pk=pk)
        return render(request, 'events-detail.html', {
            'event': p,
        })


class AboutPage(generic.TemplateView):
    template_name = "about.html"
