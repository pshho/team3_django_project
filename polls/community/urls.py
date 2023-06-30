from django.urls import path

from . import views

app_name = 'community'

urlpatterns = [
    path('board_free/', views.board_free, name='free'),  # 자유게시판
    path('board_free_recommend/', views.board_free_recommend, name='free_recommend'),  # 자유게시판 추천수 보기
    path('<int:free_board_id>/', views.board_free_detail, name='detail'),  # 게시판 상세보기
    path('board_free_write/',views.board_free_write, name='write'), # 게시판 작성
    path('board_free_update/<int:free_board_id>',views.board_free_update, name='update'), # 게시판 수정
    path('comment/<int:free_board_id>/', views.comment_create, name='comment_create'), # 댓글 등록

]
