from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goals_webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'auth.views.login_user'),
    url(r'^goals/update', 'goals_mgmt.utils.update_flags'),
    url(r'^goals/', 'goals_mgmt.views.home'),
    url(r'^$', 'goals_mgmt.views.redirect'),
)
