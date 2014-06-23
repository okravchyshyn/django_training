from django.conf.urls import url

from tw_study import views


urlpatterns = [
    # ex: /polls/
    url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    # ex: /polls/5/
    url(r'^index/$', views.index, name='index'),
    # ex: /polls/5/vote/

