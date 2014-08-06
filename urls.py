from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#------------------------------------------------------------------#
# Removing "Auth" menu from admin site. 

from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()
admin.site.unregister(Group)
admin.site.unregister(User)


#------------------------------------------------------------------#

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MerkhetMarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

