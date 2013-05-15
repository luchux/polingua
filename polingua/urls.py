from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from lessons.views import exercise, exercises, submit_solution, words_training,train
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
     #url(r'^polingua/dialogue/$',dialogue),
     # url(r'^lessons/words/ajax/exercise/$',exercise),
     # url(r'^lessons/words/ajax/exercises/$',exercises),
     (r'^polingua/words/$',words_training),
     (r'^polingua/words/',words_training),
     url(r'^train/words/$',submit_solution),
     url(r'^polingua/train/api$',include(v1_api.urls)),
     url(r'^words/api/', include(v1_api.urls)),
     url(r'^polingua/stats/$',get_values),
     url(r'^polingua/train$',train),
     (r'^accounts/login/$', 'django.contrib.auth.views.login'),


    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
