from django.urls import path 
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="home" ),
    path('<int:id>/delete/',views.delete,name="home" )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns =+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
