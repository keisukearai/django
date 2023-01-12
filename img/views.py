# -*- coding: utf-8 -*-

import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import Category
import db.db_connect as db
from .common import Common

class HomeView(TemplateView):
    """
    HOMEページ
    """

    # テンプレート名
    template_name = "home.html"

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
    template_name = "blog.html"

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

        # 独自SQLを実行
        sql = "select * from img_blog b inner join img_category c on b.category_id = c.id order by b.id"
        logger.debug(sql)
        blog_list = db.execute(sql)

        # テンプレートパラメータ
        params = {
            'selected_category': 0,
            'category_list': category_list,
            'blog_list': blog_list
        }
        return render(request, self.template_name, params)

    def post(self, request):
        """
        Blogページプルダウン変更処理
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
        add_where = ""
        if category != '0':
            add_where = f"and b.category_id = { category }"

        # 独自SQLを実行
        sql = ("select * from img_blog b inner join img_category c on b.category_id = c.id "
               f"where 1=1 { add_where } "
               "order by b.id")
        logger.debug(sql)
        # SQL実行
        blog_list = db.execute(sql)

        # テンプレートパラメータ
        params = {
            'selected_category': int(category),
            'category_list': category_list,
            'blog_list': blog_list
        }
        return render(request, self.template_name, params)

class AjaxView(TemplateView):
    """
    Ajaxページ
    """

    # テンプレート名
    template_name = "ajax.html"

    def get(self, request):
        """
        Ajaxページ初期表示処理
        """

        # テンプレートパラメータ
        params = {
        }
        return render(request, self.template_name, params)

    def post(self, request):
        """
        Ajaxボタン押下処理
        """

        # ajaxパラメータ
        params = {
            'key1': 'value1',
            'key2': 'value2',
        }
        return JsonResponse(params)