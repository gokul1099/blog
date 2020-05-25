
from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name="article")
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
