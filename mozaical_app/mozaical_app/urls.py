from django.conf.urls import patterns, include, url

import moz.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mozaical_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^moz/', include(moz.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
