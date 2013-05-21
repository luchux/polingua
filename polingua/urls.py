from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from lessons.api import TranslationResource, ExerciseResource

from lessons.views import train,submit_solution

#TODO: there is a cleaner way of implement this
v1_api = Api(api_name='words')
v1_api.register(TranslationResource())
v1_api.register(ExerciseResource())

urlpatterns = patterns('',

    # words api impelements:
    #  -  /api/words/exercises
    #  -  /api/words/translates
    url(r'^api/', include(v1_api.urls)),
    url(r'^train/',train),
    url(r'^train/validate/',submit_solution),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
