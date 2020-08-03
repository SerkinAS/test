from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.template.context_processors import static
from django.urls import path
from untitled1 import settings
from .views import gallery, about_me, create_album, create_image, edit_album, delete_album, edit_image, album_view, delete_image
from django.conf.urls.static import static


urlpatterns = [
    path('', gallery),
    path('about_me/', about_me),
    path('create_album/', create_album, name = 'create_album'),
    path('create_image/', create_image, name = 'create_image'),
    path('edit_album/<int:pk>', edit_album, name = 'edit_album'),
    path('delete_album/<int:pk>', delete_album, name='delete_album'),
    path('edit_image/<int:pk>', edit_image, name = 'edit_image'),
    path('view_album/<int:pk>', album_view, name = 'album_view'),
    path('delete_image/<int:pk>', delete_image, name = 'delete_image')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)