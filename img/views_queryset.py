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

    def get(self, request):
        """
        Blogページ初期表示処理
        """
        # ログ出力
        logger = logging.getLogger('blog')

        # インスタンス生成
        common = Common()

        # カテゴリ一覧の取得
        category_list = common.get_category_list()

        # Query実行
        blog = Blog.objects.select_related('category').all().order_by("-category_id")
        # SQLの出力
        logger.debug(blog.query)
        # QuerySetへ
        blog_list = blog.values(
            'title',
            'image',
            'category__category_name'
        )
        logger.debug(blog_list)

        # テンプレートパラメータ
        params = {
            'selected_category': 0,
            'category_list': category_list,
            'blog_list': blog_list
        }
        return render(request, self.template_name, params)

    def post(self, request):
        """
        Blogページのプルダウン変更処理
        """
        # ログ出力
        logger = logging.getLogger('blog')

        # インスタンス生成
        common = Common()

        # リクエストパラメータ取得
        category = request.POST.get('category')

        # カテゴリ一覧の取得
        category_list = common.get_category_list()

        # where句条件
        in_category = category_list.values_list()
        if category != '0':
            in_category = [category]

        # Query実行
        blog_list = Blog.objects.all().select_related().filter(category_id__in=in_category).values(
            'title',
            'image',
            'category__category_name'
        )
        logger.debug(blog_list)

        # テンプレートパラメータ
        params = {
            'selected_category': int(category),
            'category_list': category_list,
            'blog_list': blog_list
        }
        return render(request, self.template_name, params)