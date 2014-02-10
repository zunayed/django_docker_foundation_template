from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^people/', 'people.views.people_page', name='people'),
    url(r'^work/', 'work.views.work_page', name='work'),
    url(r'^admin/', include(admin.site.urls)),
)
