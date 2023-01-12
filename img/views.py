from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView

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