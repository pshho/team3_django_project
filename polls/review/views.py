from django.shortcuts import render

def review_list_main(request):
    return render(request, 'review/review_list_main.html')

def review_list_jan(request):
    return render(request, 'review/review_list_jan.html')

def review_list_mama(request):
    return render(request, 'review/review_list_mama.html')

def review_list_subscription(request):
    return render(request, 'review/review_list_subscription.html')

def review_detail(request):
    return render(request, 'review/review_detail.html')
