from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from pic import views

urlpatterns = [
    path('pic/', views.PicList.as_view()),
    path('pic/<int:pk>/', views.PicDetail.as_view()),
    path('pic/delpic/', views.PicDel.as_view()),
    path('pic/search/', views.PicSearch.as_view()),
    path('pic/calhash/', views.CalImageHash.as_view()),
    path('pic/calhashs/', views.CalImageHashs.as_view()),
    path('pic/ban/', views.AddToBanList.as_view()),
    path('pic/cancleban/', views.RemFromBanList.as_view()),
    path('pic/banlist/', views.ViewBanList.as_view()),
    path('pic/viewdup/', views.QueryDupAll.as_view()),
    re_path(r'^pic/query/(?P<pk>\d+)?$', views.QueryDupGtNum.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
