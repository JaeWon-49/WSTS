# my_web_service/urls.py
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. 문제 재현용 앱 (기존)
    path('issue/', include('service_app.urls')), 
    
    # 2. Gunicorn 적용 비교용 앱 (신규)
    path('solved/', include('service_ts.urls')), 
]