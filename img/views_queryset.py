# -*- coding: utf-8 -*-

import logging
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog
from .common import Common

class HomeView(TemplateView):
    """
    HOMEページ
    """

    # テンプレート名
    template_name = "q/home.html"

    def get(self, request):
        """
        HOMEページ初期表示処理
        """

        # テンプレートパラメータ
        params = {
        }
        return render(request, self.template_name, params)

class BlogView(TemplateView):
    """
    Blogページ
    """

    # テンプレート名
    template_name = "q/blog.html"
    # 1ページ表示件数
    paginate_by = 3

    def get(self, request):
        """
        Blogページ初期表示処理
        """
        # ログ出力
        logger = logging.getLogger('blog')

        # インスタンス生成
        common = Common()

        # リクエストパラメータ取得
        category = request.GET.get('category', '')
        # page番号
        page = request.GET.get('page')

        # カテゴリ一覧の取得
        category_list = common.get_category_list()

        # Query実行
        in_category = category_list.values_list('id')
        if category != '':
            in_category = [category]

        print(f"in_category:{ in_category }")
        print(f"category:{ category }")

        # Query実行
        blog_qs = Blog.objects.all().select_related().filter(category_id__in=in_category).values(
            'title',
            'image',
            'category__category_name'
        )
        logger.debug(blog_qs)

        # ページネーション
        blog_paginator = Paginator(blog_qs, self.paginate_by)

        try:
            page_obj = blog_paginator.page(page)
        except PageNotAnInteger:
            page_obj = blog_paginator.page(1)
        except EmptyPage:
            page_obj = blog_paginator.page(blog_paginator.num_pages)

        # テンプレートパラメータ
        params = {
            'selected_category': category,
            'category_list': category_list,
            'page_obj': page_obj
        }
        return render(request, self.template_name, params)