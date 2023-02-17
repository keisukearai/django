from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

# アプリケーション名
app_name = 'img'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ajax', views.AjaxView.as_view(), name='ajax'),
    path('blog', views.BlogView.as_view(), name='blog'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
