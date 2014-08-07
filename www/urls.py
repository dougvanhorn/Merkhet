from django.contrib import admin
from django.conf.urls import patterns, include, url


# This is no longer needed in Django 1.7.
#admin.autodiscover()


#------------------------------------------------------------------#

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    # Eventually we'll include our application.
    #url(r'^', include(merkhet.urls)),
)

