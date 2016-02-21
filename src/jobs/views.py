from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin


from django.utils import timezone
from django.views import generic

from .models import Job



class IndexView(generic.ListView):
    template_name = 'jobs/index.html'
    context_object_name = 'latest_job_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Job.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Job
    template_name = 'jobs/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Job.objects.filter(pub_date__lte=timezone.now())