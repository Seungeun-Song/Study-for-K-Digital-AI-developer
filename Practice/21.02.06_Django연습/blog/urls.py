# re_path() - django.conf.urls.url()와 동일
# archive = 전체 글 조회 뿐만 아니라 년도, 월, 일 각각으로 나누어서 해당하는 게시물을 조회 가능

from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    #/blog/
    path('', views.PostLV.as_view(), name='index'),
    #/blog/post/
    path('post/', views.PostLV.as_view(), name='post_list'),
    #/blog/post/django-example(slug)/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    #/blog/archive/
    path('archive/', views.PostAV.as_view(), name='post_archive'),
    #/blog/archive/2019/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    #/blog/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    #/blog/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    #/blog/archive/today/
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),
]

'''URL /blog/post/슬러그/요청을 처리할 뷰 클래스를 PostDV 로 지정한다. 
URL 패턴의 이름은 'blog:post_detail' 이 된다. 한글이 포함된 슬러그는 처리를 못한다. 
<slug> 컨버터는 '[-a-zA-Z0-9_]+' 만 인식한다.'''