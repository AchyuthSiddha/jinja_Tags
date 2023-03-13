from django.urls import path
from csk.views import *
app_name='somrthing'
urlpatterns=[
    path('CskTeam/',CskTeam,name='CskTeam'),
]