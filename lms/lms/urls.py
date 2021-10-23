from django.contrib import admin
from django.urls import path
from django.conf.urls import include

import school
import college 
urlpatterns = [
    path('', include('school.urls')),
    path('college/',include('college.urls')),
    path('admin/', admin.site.urls),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)