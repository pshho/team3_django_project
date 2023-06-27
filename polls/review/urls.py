from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    path('review_main/', views.review_list_main, name='review_main'), # 거래 후기 메인
    path('review_jan/', views.review_list_jan, name='review_jan'), # 거래후기전세
    path('review_mama/', views.review_list_mama, name='review_mama'), # 거래후기매매
    path('review_subscription/', views.review_list_subscription, name='review_subscription'), # 거래후기청약
    path('review_detail/', views.review_detail, name='review_detail'), # 거래후기보기

]
