from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


import profiles.urls
import accounts.urls
import jobs.urls
import rest_framework

import tinymce
from . import views


from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


import jobs.models
import jobs.crunchbase_models
import jobs.model_acquisitions
import jobs.model_investments
import jobs.model_additions

# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         User = get_user_model()

#         model = User
#         fields = ('url', 'email', 'is_staff', 'is_superuser')

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     User = get_user_model()

#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
# router.register(r'jobs', jobs.models.JobViewSet)
# router.register(r'events', jobs.models.EventViewSet)
# router.register(r'companies', jobs.crunchbase_models.CompanyViewSet)
router.register(r'support', jobs.models.SupportTokenViewSet)


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^support$', views.SupportPage.as_view(), name='support_handler'),
    url(r'^example$', views.ExamplePage.as_view(), name='example_handler'),
    url(r'^support_maker$', views.SupportMaker, name='support_maker'),

    url(r'^v/(?P<name>\w+)/$', views.DemoPage.as_view(), name='demo'),


    url(r'^analytic/$', views.AnalyticHandler, name='analytic_handler'),


    url(r'^jobs/$', login_required(views.JobsPage.as_view()), name='jobs'),
    url(r'^jobs/(?P<pk>\d+)/$', login_required(views.JobsDetailPage.as_view()), name='jobs-detail'),

    url(r'^events/$', login_required(views.EventsPage.as_view()), name='events'),
    url(r'^events/(?P<pk>\d+)/$', login_required(views.EventsDetailPage.as_view()), name='events-detail'),

    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),

    #url(r'^jobs/', include(jobs.urls, namespace='jobs')),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
