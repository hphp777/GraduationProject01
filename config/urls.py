"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # 첫번째 인자에 해당하는 url을 입력했을 때 두번째 인자에 해당하는 url.py로 간다.
    # 그 urls.py를 뭐라고 부르느냐? 가 namespace
    path("", include("core.urls", namespace="core")),  # 딱 첫 화면에 띄우는 것
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path('admin/', admin.site.urls),
]

# if settings.DEBUG:  # develop모드이면
#     # 리스트 이름 변경하면 안됨
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
