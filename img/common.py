# -*- coding: utf-8 -*-
import logging

from .models import Category

class Common:
    """
    共通処理
    """

    def get_category_list(self):
        """
        カテゴリ一覧取得処理
        """
        # ログ出力
        logger = logging.getLogger('blog')

        category_list = Category.objects.order_by('-id')
        logger.debug(Category.objects.order_by('-id').query)

        return category_list