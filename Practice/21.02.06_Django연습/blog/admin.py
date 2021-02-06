from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

    '''
    admin.site.register() 함수를 사용해도 되지만, 데코레이터를 사용하면 더 간단하다.
    PostAdmin 클래스는 Post 클래스가 Admin 사이트에서 어떤 모습으로 보여줄지를 정의하는 클래스이다.
    modify_dt 컬럼을 사용하는 필터 사이드바를 보여주도록 지정한다.
    검색박스를 표시하고, 입력된 단어는 title 과 content 칼럼에서 검색하도록 한다.
    slug 필드는 title 필드를 사용해 미리 채워지도록 한
    '''