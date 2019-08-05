from django.urls import path
from .views import portfolio_index, project_details, project_technology
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', portfolio_index, name='portfolio_index'),
    path('<int:pk>/', project_details, name='project_details'),
    path('<tech>/', project_technology, name='project_tech'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
