from django.urls import path
from polls import views


app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),      # /polls/
    path('<int:question_id>/', views.detail, name='detail'),       # /polls/5/ 5=다섯번째 질문이라는 경로
    path('<int:question_id>/results/', views.results, name='results'),     # /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # /polls/5/vote/
]       # .html 템플릿을 처리



'''views.index 이렇게 오면 name='index'이렇게 대응(처리)할 거예요. 
 <int:question_id>/ 이렇게 오면 views.detail, name='detail' 이렇게 대응할 거예요..
 <int:question_id>/results/ 이렇게 오면 views.results, name='results'이렇게 대응할 거예요.
 <int:question_id>/vote/ 이렇게 오면 views.vote, name='vote 이렇게 대응할거예요.
  ==> 라는 뜻 '''