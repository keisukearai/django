from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog
from .models import Category

""" Django 管理サイト名変更 """
admin.site.site_header = 'ブログ管理サイト'

""" サイト管理名変更 """
admin.site.index_title = 'テーブル一覧'

class BlogAdmin(admin.ModelAdmin):

    def blog_image(self, obj):
        # 画像の存在チェック
        if obj.image:
            return mark_safe(f'<img src="{ obj.image.url }" style="width:5rem;">')
        return ''

    list_display = ('title', 'blog_image')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)