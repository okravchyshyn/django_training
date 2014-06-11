from django.conf.urls import url

from blog import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^add_new/$', views.add_new, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/edit/$', views.edit, name='results'),
    # ex: /polls/5/vote/
]

