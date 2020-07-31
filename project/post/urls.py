from django.urls import path
from post import views

app_name = 'post'
urlpatterns = [
    # path('list/',views.post_list, name='post_list'),
    path('',views.main, name='main'),
    path('list/',views.list,name='list'),
    path('quiz/<int:pk>/',views.quiz,name='quiz'),
    path('detail/',views.detail, name='detail'),

]