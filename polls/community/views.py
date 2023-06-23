from django.shortcuts import render

# Create your views here.
def board_free(reqeust):
    return render(reqeust, 'community/board_free/board_free.html') # 자유게시판

def board_free_detail(request):
    return render(request, 'community/board_free/board_free_detail.html') # 게시판 상세보기

def board_free_write(request):
    return render(request, 'community/board_free/board_free_write.html') # 게시판 작성

def board_free_update(request):
    return render(request, 'community/board_free/board_free_update.html') # 게시판 수정