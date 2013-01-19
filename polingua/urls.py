from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from lessons.views import train, results, dialogue, exercise, exercises, submit_solution
from statistics.views import get_values

from tastypie.api import Api
from lessons.api import TranslationResource, ExerciseResource

v1_api = Api(api_name='v1')
v1_api.register(TranslationResource())
v1_api.register(ExerciseResource())

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'polingua.views.home', name='home'),
    # url(r'^polingua/', include('polingua.foo.urls')),
     url(r'^polingua/train/$',train),
     url(r'^polingua/dialogue/$',dialogue),
     url(r'^polingua/results/$',results),
     url(r'^polingua/exercises/$',exercises),
     url(r'^polingua/exercise/$',exercise),
     url(r'^polingua/train/ajax/validate/$',submit_solution),
     #url(r'^polingua/train/api$',include(v1_api.urls)),
     url(r'^api/', include(v1_api.urls)),
     url(r'^polingua/stats/$',get_values),
     #url(r'^ajax/train$',ajax_train),


    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
