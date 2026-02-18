from django.contrib import admin
from django.urls import path, include

# ✅ ADD THESE TWO LINES
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]

# ✅ THIS LINE IS REQUIRED TO SHOW UPLOADED FILES
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
