from django.contrib import admin

# Register your models here.


from polls.models import Question, Choice            # models.py에 저장한 Question, Choice를 불러오겠다는


admin.site.register(Question)                               # admin 사이트에 등록하겠다는
admin.site.register(Choice)
