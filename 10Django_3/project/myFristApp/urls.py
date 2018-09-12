from django.conf.urls import url
from .views import index, cookietest, redirect1,\
    redirect2, main , login ,loginRedirect

urlpatterns = [
    url(r'^$', view=index),

    url(r'^cookietest/$', view=cookietest),

    url(r'^redirect1/', view=redirect1),

    url(r'^redirect2/', view=redirect2),

    url(r'^main/', view=main),

    url(r'^login/', view=login),

    url(r'^loginRedirect/',view=loginRedirect)
]
