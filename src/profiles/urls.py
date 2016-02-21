from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^me$', views.ShowProfile.as_view(), name='show_self'),
    url(r'^me/edit$', views.EditProfile.as_view(), name='edit_self'),
    url(r'^(?P<slug>[\w\-]+)$', login_required(views.ShowProfile.as_view()),
        name='show'),
]
