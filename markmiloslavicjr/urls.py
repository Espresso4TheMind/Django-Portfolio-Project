from django.contrib import admin
from django.urls import path, include
from .views import homepage, about, events, contact

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('events/', events, name='events'),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
