from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from games.views import GameViewSet
from apps.games.views import BuyGameView


router = DefaultRouter()
router.register(r'game', GameViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls), name='game'),
    path('buy/', BuyGameView.as_view(), name='buy')
]
