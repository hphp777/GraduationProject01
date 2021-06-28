from django.urls import path
from django.urls.resolvers import URLPattern
from rooms import views as room_views

app_name = "core"

# 첫번째 인자로 url을 받았을 때 홈뷰를 띄운다.
# 띄우는 함수가 as_view
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
