from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from . import views_queryset as vq

# アプリケーション名
app_name = 'img'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ajax', views.AjaxView.as_view(), name='ajax'),
    path('blog', views.BlogView.as_view(), name='blog'),
    path('q', vq.HomeView.as_view(), name='q_home'),
    path('q/blog', vq.BlogView.as_view(), name='q_blog'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
