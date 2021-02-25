from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView #클래스형 제네릭 뷰 임포트하기위해 ListView, DetailView클래스 임포트
from bookmark.models import Bookmark #테이블 조회를 위해 모델클래스 임포트

class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark