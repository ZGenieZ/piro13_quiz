from django.shortcuts import render
from django.contrib.auth.models import User


# from account.models import *
# Create your views here.
# def post_list(request):
#     quizs = Account.objects.all().quizs #퀴즈 모델 갖고 오기
#     #출제자 갖고 와야 하는 부분
#     return render(request,'post/post_list.html',
#                   {
#                       'quizs': quizs
#                   })
def main(request):
    return render(request, 'post/main.html')

def list(request):
    users = User.objects.all()
    data = {
       'users': users
    }
    return render(request, 'post/list.html',data)


def quiz(request, pk):
    # quiz = User.objects.quizs.get(pk=pk)
    user = User.objects.get(pk=pk)
    quiz = user.quizs
    data = {
        'user':user,
        'quiz': quiz
    }
    return render(request, 'post/quiz.html',data)


def detail(request):
    return render(request, 'post/detail.html')
# def client_list(request):
#     qs = Client.objects.all()
#     return render(request, 'client/client_list.html',
#                   {'clients': qs,
#                    }
#                   ) user.quizs.pk = quiz.pk

