from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import request
from django.shortcuts import render, redirect,get_object_or_404
from django.utils import timezone

from community.forms import FreeForm, AnswerForm
from community.models import Free_Board, Answer

def board_free(request):
    question_list = Free_Board.objects.order_by('-b_regdate')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'community/board_free/board_free.html', context) # 자유게시판

def board_free_recommend(request):
    question_list = Free_Board.objects.order_by('-b_recommend')
    page = request.GET.get('page', '1')
    paginator = Paginator(question_list, 10)
    text = paginator.get_page(page)

    context = {'question_list': text}
    return render(request, 'community/board_free/board_free.html', context) # 자유게시판

def board_free_detail(request, free_board_id):
    free_board = get_object_or_404(Free_Board, id=free_board_id)
    free_board.b_hit += 1
    free_board.save()

    # AnswerForm과 연관된 데이터 필터링
    answers_list = Answer.objects.filter(board_id=free_board_id)

    context = {'free_board': free_board, 'answers_list':answers_list}
    return render(request, 'community/board_free/board_free_detail.html', context) # 게시판 상세보기

def board_free_write(request):
    if request.method == "POST":
        form = FreeForm(request.POST)

        if form.is_valid():  # 폼이 유효성 검사를 통과했다면
            free = form.save(commit=False)
            free.user = request.user
            free.b_regdate = timezone.now()
            form.save()

            return redirect('community:free')
    else:
        form = FreeForm()

    context = {'form': form}

    return render(request, 'community/board_free/board_free_write.html',context) # 게시판 작성


def comment_create(request, free_board_id):
    # 댓글 등록
    free_board = get_object_or_404(Free_Board, pk=free_board_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user   # 세션
            comment.create_date = timezone.now()
            comment.question = free_board
            comment.board_type = 'Free_Board'
            comment.board_id = free_board_id
            comment.save()
            return redirect('community:detail', free_board_id=free_board_id)
    else:
        form = AnswerForm()

    context = {'free_board':free_board, 'form':form}
    return render(request, 'community/board_free/board_free_detail.html', context)

def board_free_update(request, free_board_id):
    free_board = get_object_or_404(Free_Board, pk=free_board_id)

    if request.method == "POST":
        form = FreeForm(request.POST, instance=free_board)

        if form.is_valid():
            free = form.save(commit=False)
            free.b_modifydate = timezone.now()
            free.user = request.user
            free.save()

            return redirect('community:detail', free_board_id=free_board_id)

    else:
        form = FreeForm(instance=free_board)

    context = {'form': form, 'free_board':free_board}
    return render(request, 'community/board_free/board_free_update.html', context) # 게시판 수정
