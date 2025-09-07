from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})

"""
설명을 하자면 다음과 같다.
일단 post_list라는 함수를 만들었다.
request(요청)을 받아와서, render라는 메서드를 호출한다.
* render -> 템플릿을 랜더링해서 HttpResponse를 만들어주는 '지름길(shortcut) 함수'
여튼 자세한건 아래에 gpt의 응답을 참고하고,
보다시피 return을 받아 blog/post_list.html을 보여주는 함수이다.
"""