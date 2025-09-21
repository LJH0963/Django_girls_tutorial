from django.contrib import admin

# Register your models here.

from .models import Post        # 같은 폴더에 있으므로 '.' 사용

admin.site.register(Post)