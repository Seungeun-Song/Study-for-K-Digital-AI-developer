from django.urls import path
from bookmark.views  import BookmarkLV, BookmarkDV

app_name = 'bookmark'
urlpatterns = [
      #/bookmark/
     path('', BookmarkLV.as_view(), name='index'),
     # /bookmark/3/
     path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]

