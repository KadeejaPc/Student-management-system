from django.conf.urls import url,include
from faculty_advstudent import views

urlpatterns =[
    url('^vpro/',views.vpro,name='vpro'),
    url('^postfeed/',views.postfeed,name='postfeed'),
    url('^vinternal/',views.vinternal,name='vinternal'),
    url('^vatt/',views.vatt,name='vatt'),
    url('^vnot/', views.vnot, name='vnot'),
    url(r'^rply/(?P<idd>\w+)', views.rply, name='rply'),



    ]