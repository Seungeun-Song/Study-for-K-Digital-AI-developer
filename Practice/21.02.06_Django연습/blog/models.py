from django.db import models

# Create your models here.
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)  #verbose_name : 사용자가 읽기 쉬운 모델 객체의 이름으로 관리자 화면 등에서 표시
    #slug = 글이 작성된 시각, 글이 수정된 시각, 제목, 설명, 내용, 각각의 글을 가리킬 별칭, slug는 게시물 검색에 사용
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField("DESCRIPTION", max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now = True)

    class Meta:
        verbose_name = 'post' #verbose_name : 테이블 단수 별칭
        verbose_name_plural = 'posts' #verbose_name_plural : 테이블 복수 별칭
        db_table = 'blog_posts' #디폴트는 앱명_모델명(blog_post)
        ordering = ('-modify_dt',) #출력 시 modify_dt를 기준으로 내림차순 정렬

    def __str__(self): #__str__() 메소드는 객체를 문자열로 표현할 때 사용하는 함수
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))  #post_detail - urls.py의 post_detail(PodstDV 뷰와 연결되는 url)과 연결
    # blog:post_detail = url 패턴이름. url.py blog에서 이름이 post_detail인
    '''get_absolute_url
    페이지를 이동하는 방법중 하나로서 a 태그의 href에서 get_absolute_url를 호출하여 사용한다. 
    {% url %}을 사용하여 get_absolute_url을 대체할 수 있다.
    > reverse 함수를 통해서 호출되는 함수와, 파라미터를 지정할 수 있다.'''

    '''
      {% for post in posts %}
      <h2><a href="{{ post.get_absolute_url }}">{{post.title}}</a></h2>
      <!-- modify_date 를 July 05, 2017 형태로 표시 -->
      {{ post.modify_date|date:"N d, Y"}}
      <p>{{ post.description }}</p>
    {% endfor %}'''

    '''특정 모델에 대한 Detail뷰를 작성할 경우, Detail뷰에 대한 URLConf설정을 하자마자,
    필히 get_absolute_url설정을 해주세요. 코드가 보다 간결해집니다'''
    # reverse() = 리턴형식

    def get_previous(self):
        return self.get_previous_by_modify_dt()
        # get_previous() 는 장고의 내장함수, modify_dt()를 기준으로 최신포스트를 반환

    def get_next(self):
        return self.get_next_by_modify_dt()
        # get_next() 는 modify_dt 라는 DateTimeField를 기준으로 다음 객체를 반환한다.






'''★ 슬러그(Slug)란?
슬러그는 페이지나 포스트를 설명하는 핵심 단어의 집합이다.
보통 슬러그는 페이지나 포스트의 제목에서 조사, 전치사, 쉼표, 마침표 등을 빼고 띄어쓰기는 하이픈(-)으로 대체해서 만들며 URL 에 사용된다.
슬러그를 URL에 사용함으로써, 검색 엔진에서 더 빨리 페이지를 찾아주고 검색엔진의 정확도를 높여준다.'''

'''★ SlugField 필드 타입
슬러그는 보통 제목의 단어들을 하이픈으로 연결해 생성하며, URL에서 pk 대신 사용되는 경우가 많다.
pk 를 사용하면 숫자로만 되어있고, 그 내용을 유추하기는 어렵지만, 슬러그를 사용하면 보통의 단어들이라서 이해하기 쉽기 때문이다.
SlugField 필드의 디폴트 길이는 50이며, 해당 필드에는 인덱스가 디폴트로 생성된다.'''