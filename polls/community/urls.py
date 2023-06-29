from django.urls import path

from . import views

app_name = 'community'

urlpatterns = [
    path('board_free/', views.board_free, name='free'),  # 자유게시판
    path('board_free_detail/', views.board_free_detail, name='detail'),  # 게시판 상세보기
    path('board_free_write/',views.board_free, name='write'), # 게시판 작성
    path('board_free_update/',views.board_free_update, name='update'), # 게시판 수정
]
