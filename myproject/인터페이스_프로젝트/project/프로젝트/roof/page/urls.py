from django.urls import re_path
from page import views



app_name = 'page'
urlpatterns = [

    #/page/member/yonghyun/
    re_path(r'^member/(?P<slug>[-\w]+)/$', views.PageMemberDV.as_view(), name='member_detail'),

    #/page/member/yonghyun/game/
    re_path(r'^member/(?P<slug>[-\w]+)/(?P<category_id>[-\w]+)/$', views.PageCategoryDV.as_view(), name='member_category_detail'),
    
    #/page/member/yonghyun/game/game-title/
    re_path(r'^member/(?P<member_id>[-\w]+)/(?P<category_id>[-\w]+)/(?P<slug>[-\w]+)/$', views.PageDV.as_view(), name='member_post_detail'),    

    #/page/member/yonghyun/game/game-title/game-photo-title/
    re_path(r'^member/(?P<member_id>[-\w]+)/(?P<category_id>[-\w]+)/(?P<post_id>[-\w]+)/(?P<slug>[-\w]+)$', views.PagePhotoDV.as_view(), name='member_photo_detail'),

    #/page/tag/supermario/
    re_path(r'^tag/(?P<slug>[-\w]+)/$', views.TagDV.as_view(), name='tag_detail'),

    #/page/category/game/
    re_path(r'^category/(?P<slug>[-\w]+)/$', views.CaDV.as_view(), name='category_detail'),

    #/page/search/
    re_path(r'^search/$', views.SearchFormView.as_view(), name='search'),

]

