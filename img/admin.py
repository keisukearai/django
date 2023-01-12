from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Blog

""" Django 管理サイト名変更 """
admin.site.site_header = 'ブログ管理サイト'

""" サイト管理名変更 """
admin.site.index_title = 'テーブル一覧'

class BlogAdmin(admin.ModelAdmin):

    def blog_image(self, obj):
        return mark_safe('<img src="{}" style="width:5rem;">'.format(obj.image.url))

    list_display = ('title', 'blog_image')

admin.site.register(Blog, BlogAdmin)