from django.conf import settings
from django.db import models
from django.utils import timezone




# 블로그 글을 Post하는 model 생성
## 모델이라는 객체를 정의한다.(class = 나 객체를 정의한다! / Post=model의 이름, 항상 첫자는 대문자로)
class Post(models.Model):
    """
    정의해야 하는 것들 :
    author / title / text = 블로그 글의 본문 / created_date / published_date 
    """
    # models = Django의 모델임을 나타내며, Post가 데이터베이스에 저장됨을 의미
    ## 이제 아래부터는 속성을 정의하는 것이다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings.AUTH_USER_MODEL = 커스텀 유저의 모델로 변경해도 바꿔도 호환되도록 한 것.
    title = models.CharField(max_length = 200)  # CharField = 글자 수가 제한된 텍스트를 의미
    text = models.TextField()       # Textfield = 글자 수 제한 없음
    created_date = models.DateField(        # 연월일까지만 저장
        default=timezone.now
    )
    published_date = models.DateTimeField(      # 날짜 + 시간 저장
        blank=True, null=True
    )

    # 이제 글을 실제 발행하면, 그 발행한 글의 날짜를 채워주는 함수가 필요
    ## 따라서 publish라는 함수를 만들어, 그 안에 값을 넣도록 한다.

    def publish(self):      # self = 자기 자신을 가리키는 참조(reference)
        self.published_date=timezone.now()
        self.save()

    def __str__(self):      # 파이썬에서 객체를 문자열로 표현하기 위한 특별 메서드(던더 메서드)
        return self.title