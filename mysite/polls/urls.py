from django.urls import path

from . import views

urlpatterns = [
    #path의 인자로 route와 view, 2개의 선택 가능한 인수로 kwargs, name
    #route : 요청된 URL을 각 패턴과 리스트의 순서대로 비교합니다
    #view: 첫 번째 인자에서 일치하는 패턴을 찾으면 뒤에서 설명
    #kargs: view에 사전형으로 전달(이 튜토에서는 사용 안함)
    #name: URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다.
    #       이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와줍니다.
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
