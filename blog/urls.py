from django.urls import path
from blog.views import blog_index, blog_detail, blog_tags
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('<int:pk>/', blog_detail, name='blog_detail'),
    path('<tags>/', blog_tags, name='blog_tags'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
