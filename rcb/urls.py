from django.urls import path
from rcb.views import *
app_name='Nothing'
urlpatterns=[
    path('RcbTeam/',RcbTeam,name='RcbTeam'),
]