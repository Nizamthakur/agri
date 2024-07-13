
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homepage,name='homePage'),
    path('', views.index_view, name='index'),
    path('', views.get_quote, name='get_quote'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
