from django.shortcuts import render

def index(request):
    return render(request, 'poll/index.html')
def board(request):
    return render(request, 'poll/board.html')
