from django.urls import path,re_path
from django.conf.urls import url
from .views import hello, current_datatime,hours_ahead
from .views import ListSongsView

urlpatterns=[

path('',ListSongsView.as_view(), name="songs-all"),
re_path('hello/$',hello),
re_path('time/$',current_datatime),
re_path(r'time/plus/(\d{1,2})/',hours_ahead),
]