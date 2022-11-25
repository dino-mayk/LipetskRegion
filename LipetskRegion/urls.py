from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('celebrities/', include('celebrities.urls'), name='celebrities'),
    path('landmarks/', include('landmarks.urls'), name='landmarks'),
    path('feedback/', include('feedback.urls'), name='feedback'),
    path('admin/', admin.site.urls, name='admin'),
    path('grappelli/', include('grappelli.urls'), name='grappelli'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
